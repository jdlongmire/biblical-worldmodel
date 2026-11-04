"""Validate locally staged IGSR VCF provenance before analysis.

Usage: python scripts/verify_igsr_input.py /path/to/chr22.vcf.gz
Never silently download multi-gigabyte files or infer provenance from filename.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

def verify(path):
    path=Path(path)
    digest=hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda:source.read(1024*1024),b""):
            digest.update(chunk)
    with gzip.open(path,"rt",encoding="utf-8") as stream:
        header=[]
        for line in stream:
            if line.startswith("##"):
                if len(header)<20: header.append(line.strip())
            elif line.startswith("#CHROM"):
                fields=line.rstrip("\n").split("\t")
                if len(fields)<10: raise ValueError("no genotype columns")
                return {"filename":path.name,"sha256":digest.hexdigest(),
                        "size_bytes":path.stat().st_size,
                        "samples":len(fields)-9,"header_excerpt":header}
            else:
                raise ValueError("VCF header missing")
    raise ValueError("VCF column header not found")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("vcf",help="Local BGZF/gzip VCF, not a remote URL")
    args=parser.parse_args()
    print(json.dumps(verify(args.vcf),indent=2))
