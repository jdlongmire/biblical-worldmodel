#!/usr/bin/env python3
"""Verify imported bridge artifact hashes, links, and optional original checkout."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = '04-work-packages/WP-BWM-0004-repository-foundation/migration.json'


def verify(root=ROOT, source_root=None):
    errors = []
    manifest = json.loads((root / MANIFEST).read_text())
    records = manifest['transfers']
    if len(records) != 4 or len({r['source_path'] for r in records}) != 4:
        errors.append('Expected four unique source artifacts')
    for rec in records:
        target = root / rec['target_path']
        if not target.is_file():
            errors.append(f'Missing target: {target}'); continue
        if hashlib.sha256(target.read_bytes()).hexdigest() != rec['target_sha256']:
            errors.append(f'Target digest mismatch: {target}')
        text = target.read_text()
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if '://' in link or link.startswith('#'):
                continue
            resolved = (target.parent / link.split('#')[0]).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f'Broken or external local link: {target}: {link}')
        if source_root:
            head = subprocess.check_output(['git', '-C', str(source_root), 'rev-parse', 'HEAD'], text=True).strip()
            if head != rec['source_commit']:
                errors.append('Source checkout revision differs from recorded revision')
            original = (source_root / rec['source_path']).read_bytes()
            if hashlib.sha256(original).hexdigest() != rec['source_sha256']:
                errors.append(f'Source digest mismatch: {rec["source_path"]}')
            expected = original.decode().replace('(../WP-BRIDGE-0002-biblical-worldmodel-publication.md)', '(../WP-BWM-0001-public-site-standup/requirements.md)').replace('(./WP-BRIDGE-0002-biblical-worldmodel-publication.md)', '(../WP-BWM-0001-public-site-standup/requirements.md)')
            if text != expected:
                errors.append(f'Unrecorded content transformation: {target}')
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path)
    args = parser.parse_args()
    errors = verify(source_root=args.source_root)
    for error in errors:
        print('FAIL:', error)
    if not errors:
        print('PASS: four migrated artifact digests and local links' + ('; source revision and exact transformations verified' if args.source_root else ''))
    raise SystemExit(bool(errors))
