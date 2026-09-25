# Data

Raw and processed market data are intentionally not committed by default.

The pipeline should store:

- raw API responses in `data/raw/`
- cleaned analytical tables in `data/processed/`

Never commit API keys or private credentials.

The project is designed to preserve source data separately from derived features so that transformations remain reproducible.
