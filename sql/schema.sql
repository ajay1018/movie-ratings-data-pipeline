CREATE TABLE IF NOT EXISTS movies (
  movie_id   INT PRIMARY KEY,
  title      TEXT NOT NULL,
  year       INT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS genres (
  movie_id INT REFERENCES movies(movie_id),
  genre    TEXT,
  PRIMARY KEY (movie_id, genre)
);

CREATE TABLE IF NOT EXISTS ratings (
  movie_id INT REFERENCES movies(movie_id),
  rating   NUMERIC(3,1),
  votes    INT,
  last_updated TIMESTAMP DEFAULT NOW(),
  PRIMARY KEY (movie_id)
);

CREATE INDEX IF NOT EXISTS idx_ratings_votes ON ratings(votes DESC);
CREATE INDEX IF NOT EXISTS idx_movies_year ON movies(year);
