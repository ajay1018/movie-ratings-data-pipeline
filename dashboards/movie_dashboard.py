import pandas as pd
import streamlit as st

st.set_page_config(page_title="Movie Ratings Dashboard", layout="wide")
st.title("🎬 Movie Ratings Dashboard")

df = pd.read_csv("data/processed/clean_ratings.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Movies", f"{len(df):,}")
col2.metric("Avg Rating", f"{df['rating'].mean():.2f}")
col3.metric("Total Votes", f"{df['votes'].sum():,}")

st.subheader("Ratings by Genre")
genre_stats = df.groupby('genre', dropna=False)['rating'].mean().sort_values(ascending=False).reset_index()
st.bar_chart(genre_stats.set_index('genre'))

st.subheader("Top 10 by Rating")
top10 = df.sort_values(['rating','votes'], ascending=[False, False]).head(10)
st.dataframe(top10, use_container_width=True)

st.caption("Data: sample dataset included for demo. Replace with real ETL output when ready.")
