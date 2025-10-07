"""Extract layer
Currently uses local CSV as a stand-in for API pulls (TMDB/IMDb). This keeps the repo runnable.
Replace `read_csv` with API client calls later.
"""
from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

def run():
    src = RAW_DIR / "sample_ratings.csv"
    df = pd.read_csv(src)
    # Save a normalized JSON too (looks nice in repo)
    (RAW_DIR / "sample_ratings.json").write_text(df.to_json(orient="records", indent=2), encoding="utf-8")
    print(f"[extract] rows: {len(df)} -> {src} & JSON")

if __name__ == "__main__":
    run()
