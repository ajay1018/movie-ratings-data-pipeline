import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()  # reads .env if present

PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
PG_DB   = os.getenv("PG_DB", "movies")
PG_USER = os.getenv("PG_USER", "postgres")
PG_PW   = os.getenv("PG_PASSWORD", "postgres")

ENGINE = create_engine(f"postgresql+psycopg2://{PG_USER}:{PG_PW}@{PG_HOST}:{PG_PORT}/{PG_DB}", future=True)

def ensure_schema():
    with open("sql/schema.sql", "r", encoding="utf-8") as f:
        schema_sql = f.read()
    with ENGINE.begin() as conn:
        for stmt in schema_sql.split(";"):
            s = stmt.strip()
            if s:
                conn.execute(text(s))

def load_tables():
    df = pd.read_csv("data/processed/clean_ratings.csv")

    movies = df[['movie_id','title','year']].drop_duplicates()
    genres = df[['movie_id','genre']].dropna().drop_duplicates()
    ratings = df[['movie_id','rating','votes']].dropna()

    movies.to_sql("movies", ENGINE, if_exists="append", index=False)
    genres.to_sql("genres", ENGINE, if_exists="append", index=False)
    ratings.to_sql("ratings", ENGINE, if_exists="append", index=False)

    print("[load] inserted:",
          len(movies), "movies /",
          len(genres), "genres /",
          len(ratings), "ratings")

if __name__ == "__main__":
    ensure_schema()
    load_tables()
