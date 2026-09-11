#!/usr/bin/env python3
"""Verify crop integrity against the retained source sheet. Requires Pillow."""
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
LIB = ROOT / 'graphics-library'
manifest = json.loads((LIB / 'manifest.json').read_text())
assert len(manifest['assets']) == 24
assert len({a['path'] for a in manifest['assets']}) == 24
for source in manifest['sources']:
    path = LIB / source['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256'], path
    with Image.open(path) as im:
        assert list(im.size) == source['dimensions'], path
for asset in manifest['assets']:
    path = LIB / asset['path']
    assert hashlib.sha256(path.read_bytes()).hexdigest() == asset['sha256'], path
    with Image.open(path) as actual, Image.open(LIB / asset['source']) as source:
        l,t,r,b = asset['crop_xyxy']
        assert 0 <= l < r <= source.width and 0 <= t < b <= source.height, path
        expected = source.crop((l,t,r,b))
        assert actual.mode == expected.mode == asset['mode'], path
        assert actual.size == expected.size == (asset['width'],asset['height']), path
        assert actual.tobytes() == expected.tobytes(), path
        assert ('A' in actual.getbands()) == asset['alpha'], path
print('PASS: 24 native-pixel crops, source/output hashes, bounds, dimensions and truthful alpha metadata')
