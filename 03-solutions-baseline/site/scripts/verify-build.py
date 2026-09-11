#!/usr/bin/env python3
"""Build strictly, verify paths, and prove a broken Markdown link rejects publication."""
from pathlib import Path
import shutil,subprocess,sys,tempfile
site=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='bwm-build-') as td:
    output=Path(td)/'site'
    subprocess.run([sys.executable,'-m','mkdocs','build','--strict','-f',str(site/'mkdocs.yml'),'-d',str(output)],check=True)
    subprocess.run([sys.executable,str(site/'scripts/verify-assets.py'),str(output)],check=True)
    # Keep source files untouched. A standalone malformed page exercises strict mode.
    negative=Path(td)/'negative';(negative/'docs').mkdir(parents=True)
    (negative/'docs/index.md').write_text('# Negative control\n\n[Broken](missing-page.md)\n')
    (negative/'mkdocs.yml').write_text('site_name: Negative control\ntheme:\n  name: material\n')
    run=subprocess.run([sys.executable,'-m','mkdocs','build','--strict','-f',str(negative/'mkdocs.yml')],capture_output=True,text=True)
    assert run.returncode!=0 and 'missing-page.md' in run.stderr,run.stdout+run.stderr
print('PASS: clean strict build and negative broken-link control')
