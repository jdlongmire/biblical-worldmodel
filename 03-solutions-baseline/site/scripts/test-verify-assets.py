"""Regression coverage for root-domain and project-subpath publications."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('verify_assets', Path(__file__).with_name('verify-assets.py'))
assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assets)


class PublicationPaths(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('hero/hero-desktop.png', 'concepts/worldmodel-layers-labelled.png', 'audiences/seeker.png'):
            target = self.root / 'graphics' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.touch()
        (self.root / 'reader').mkdir()
        (self.root / 'reader/index.html').write_text('<a href="../">Home</a>')
        (self.root / 'index.html').write_text('<a href="reader/">Reader</a>')

    def test_both_publication_bases(self):
        for base in ('/', '/biblical-worldmodel/'):
            with self.subTest(base=base):
                (self.root / '404.html').write_text(f'<a href="{base}reader/">Reader</a><img src="{base}graphics/hero/hero-desktop.png">')
                assets.verify(self.root, base)

    def test_missing_and_escaping_paths_are_rejected(self):
        for base, ref in (('/', '/missing/'), ('/', '/../outside'), ('/', '/%2e%2e/outside'), ('/', '../outside'), ('/biblical-worldmodel/', '/reader/'), ('/biblical-worldmodel/', '/biblical-worldmodel/../outside')):
            with self.subTest(base=base, ref=ref):
                (self.root / '404.html').write_text(f'<a href="{ref}">Invalid</a>')
                with self.assertRaisesRegex(AssertionError, 'Broken paths'):
                    assets.verify(self.root, base)


if __name__ == '__main__':
    unittest.main()
