#!/usr/bin/env python3
"""Build strictly, verify paths, and prove a broken Markdown link rejects publication."""
from pathlib import Path
import shutil,subprocess,sys,tempfile
from html.parser import HTMLParser
from urllib.parse import urljoin
import yaml

class Stylesheets(HTMLParser):
    def __init__(self):
        super().__init__(); self.hrefs=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag == "link" and "stylesheet" in attrs.get("rel", "").split():
            self.hrefs.append(attrs.get("href", ""))

def verify_home_styles(html, config):
    parser=Stylesheets(); parser.feed(html)
    actual=[urljoin(config["site_url"], href) for href in parser.hrefs]
    expected=[urljoin(config["site_url"], href) for href in config["extra_css"]]
    assert actual == expected, f"Homepage stylesheet order/content mismatch: {actual} != {expected}"

site=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(site/'scripts/test-verify-assets.py')],check=True)
with tempfile.TemporaryDirectory(prefix='bwm-build-') as td:
    output=Path(td)/'site'
    subprocess.run([sys.executable,'-m','mkdocs','build','--strict','-f',str(site/'mkdocs.yml'),'-d',str(output)],check=True)
    subprocess.run([sys.executable,str(site/'scripts/verify-assets.py'),str(output)],check=True)
    config=yaml.safe_load((site/'mkdocs.yml').read_text())
    html=(output/'index.html').read_text()
    verify_home_styles(html,config)
    # A missing stylesheet must fail even when every remaining link resolves.
    try:
        verify_home_styles('<link rel="stylesheet" href="styles/site.css">',config)
    except AssertionError:
        pass
    else:
        raise AssertionError('Missing homepage styles were not detected')
    print('PASS: configured homepage styles in order and missing-stylesheet control')
    # Keep source files untouched. A standalone malformed page exercises strict mode.
    negative=Path(td)/'negative';(negative/'docs').mkdir(parents=True)
    (negative/'docs/index.md').write_text('# Negative control\n\n[Broken](missing-page.md)\n')
    (negative/'mkdocs.yml').write_text('site_name: Negative control\ntheme:\n  name: material\n')
    run=subprocess.run([sys.executable,'-m','mkdocs','build','--strict','-f',str(negative/'mkdocs.yml')],capture_output=True,text=True)
    assert run.returncode!=0 and 'missing-page.md' in run.stderr,run.stdout+run.stderr
print('PASS: clean strict build and negative broken-link control')
