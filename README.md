# 🎬 Movie Ratings Data Pipeline

An end-to-end **data engineering project** that builds a complete ETL pipeline for movie analytics.  
The pipeline extracts raw movie rating data from public APIs (IMDb / TMDB), transforms and cleans it using Python,  
loads it into a **PostgreSQL** database, and finally visualizes aggregated insights through a **Streamlit dashboard**.

---

## 🧱 Architecture Overview

Data Sources (IMDb API / CSV dumps)
↓
Extract (Python Scripts)
↓
Transform (Cleaning, Type Casting, Deduplication)
↓
Load (PostgreSQL)
↓
Analytics Dashboard (Streamlit / Power BI)


🗂️ Diagrams located in `/docs`  
- `architecture_diagram.png`  
- `data_pipeline_flow.png`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Programming | Python 3.11 |
| Database | PostgreSQL |
| Orchestration | Apache Airflow |
| Containerization | Docker |
| Dashboard | Streamlit |
| Storage | CSV / S3 bucket |
| Version Control | GitHub |

---

## ⚙️ Features

- Automated **data extraction** from IMDb / TMDB API  
- Robust **data cleaning and transformation** logic using pandas  
- Incremental **load to PostgreSQL** via SQLAlchemy  
- Interactive **dashboard** for rating trends, top movies, and genres  
- Config-driven architecture with logging and error handling  
- Containerized setup using Docker  

---

## 📂 Folder Structure

movie-ratings-data-pipeline/
├── src/
│ ├── extract/ # Data extraction scripts
│ ├── transform/ # Cleaning and transformation scripts
│ └── load/ # Database loading scripts
├── data/
│ ├── raw/ # Raw source files
│ └── processed/ # Cleaned datasets
├── sql/ # Table schemas and queries
├── notebooks/ # EDA and analysis notebooks
├── dashboards/ # Dashboard screenshots / config
├── docs/ # Diagrams and docs
├── Dockerfile
├── requirements.txt
└── README.md

---

## 🚀 How to Run

### clone
- git clone https://github.com/ajay1018/movie-ratings-data-pipeline.git
- cd movie-ratings-data-pipeline

### create virtual env
- python -m venv venv
- source venv/bin/activate   # Windows: venv\Scripts\activate

### install dependencies
- pip install -r requirements.txt

### run ETL
- python src/extract/imdb_scraper.py
- python src/transform/clean_ratings.py
- python src/load/load_to_postgres.py

### launch dashboard
- streamlit run dashboards/movie_dashboard.py

---

📊 Results & Dashboard

Sample KPIs:

⭐ Top-rated movies by genre
🎯 Average rating per decade
📈 Trend of ratings over time

---

🔮 Future Improvements

- Integrate API scheduling with Airflow DAGs
- Add data quality validation using Great Expectations
- Push final dataset to BigQuery for scalability
- Deploy dashboard to Render / Streamlit Cloud

---

🧾 License

This project is licensed under the MIT License – see the LICENSE file for details.

---

## 🧱 Architecture (Mermaid)

```mermaid
flowchart TD
    A["Public APIs / CSV Dumps"] --> B["Extract (Python)"];
    B --> C["Transform (pandas)"];
    C --> D[("PostgreSQL")];
    D --> E["Streamlit Dashboard"];
```mermaid
flowchart TD
    A[Public APIs / CSV Dumps] --> B[Extract (Python)]
    B --> C[Transform (pandas)]
    C --> D[(PostgreSQL)]
    D --> E[Streamlit Dashboard]
