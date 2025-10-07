# simple docker for local demo
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash", "-lc", "streamlit run dashboards/movie_dashboard.py --server.headless=true --server.address=0.0.0.0 --server.port=8501"]
