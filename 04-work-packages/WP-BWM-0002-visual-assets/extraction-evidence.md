# Graphics decomposition — 2026-09-11

JD requested decomposition into `graphics-library/`. Retained 24 native-resolution RGB PNG crops, two original reference sheets, a contact-sheet catalog and a JSON manifest with exact coordinates, dimensions, hashes, alt text and limitations. Crops were visually inspected in the catalog and verified pixel-for-pixel against the retained sheet by `verify-extraction.py` (24/24 passed).

Extraction and verification used Pillow in an isolated temporary virtual environment; no shared Python packages or Home configuration changed. No AI regeneration, image upscaling, vector tracing or background removal occurred. The sheet's claimed SVG/transparency and larger dimensions were not treated as actual source properties. The mobile-labelled landscape panel is retained honestly as `hero-mobile-source.png`.

Run verification with Python and Pillow: `python verify-extraction.py` from this directory (the script resolves the repo independently of the current directory). The manifest is sufficient to reproduce each asset using `Image.open(source).crop(crop_xyxy).save(path)`.

This completes decomposition only. The broader package criteria for production approval, missing diagrams, portrait mobile treatment and deployed responsive integration remain pending. Source message bodies and headers are excluded from the repository.

Human-Curated, AI-Enabled (HCAE)
