from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
PROC_DIR = Path("data/processed")
PROC_DIR.mkdir(parents=True, exist_ok=True)

def run():
    df = pd.read_csv(RAW_DIR / "sample_ratings.csv")

    # basic cleaning / typing
    df['title'] = df['title'].str.strip()
    df['genre'] = df['genre'].str.strip()
    df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['votes'] = pd.to_numeric(df['votes'], errors='coerce').fillna(0).astype(int)

    # drop dupes
    df = df.drop_duplicates(subset=['movie_id'])

    # write processed
    out = PROC_DIR / "clean_ratings.csv"
    df.to_csv(out, index=False)
    print(f"[transform] rows: {len(df)} -> {out}")

if __name__ == "__main__":
    run()
