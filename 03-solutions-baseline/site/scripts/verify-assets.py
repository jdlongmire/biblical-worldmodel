#!/usr/bin/env python3
"""Reject broken local navigation and resource paths in a built site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
import sys

class Links(HTMLParser):
    def __init__(self):super().__init__();self.refs=[]
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        for key in ('src','href'):
            if key in values:self.refs.append(values[key])

root=Path(sys.argv[1]).resolve();errors=[];count=0
for page in root.rglob('*.html'):
    parser=Links();parser.feed(page.read_text());count+=1
    for ref in parser.refs:
        parts=urlsplit(ref)
        if parts.scheme or parts.netloc or not parts.path:continue
        path=unquote(parts.path)
        target=(root/path.removeprefix('/biblical-worldmodel/')) if path.startswith('/biblical-worldmodel/') else (page.parent/path)
        if target.is_dir():target=target/'index.html'
        if not target.resolve().is_relative_to(root) or not target.is_file():errors.append(f'{page.relative_to(root)}: {ref}')
assert not errors,'Broken paths:\n'+'\n'.join(errors)
for name in ('hero/hero-desktop.png','concepts/worldmodel-layers-labelled.png','audiences/seeker.png'):
    assert (root/'graphics'/name).is_file(),name
assert not (root/'graphics/references').exists(),'Reference mockups must not ship as pages'
print(f'PASS: navigation/resource paths across {count} HTML pages; graphic inclusion and reference exclusion')
