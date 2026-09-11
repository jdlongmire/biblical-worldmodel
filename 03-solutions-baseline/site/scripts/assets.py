"""Copy the product graphics library into the published site, excluding references."""
from pathlib import Path
import shutil

def on_post_build(config, **kwargs):
    root = Path(__file__).resolve().parents[3]
    library = root / 'graphics-library'
    out = Path(config['site_dir']) / 'graphics'
    for folder in ('hero', 'audiences', 'concepts', 'support', 'branding', 'icons'):
        shutil.copytree(library / folder, out / folder, dirs_exist_ok=True)
