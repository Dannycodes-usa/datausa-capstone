# 🇺🇸 DataUSA Capstone Project

This project fetches, stores, and visualizes U.S. population and income data using the DataUSA API (and a local backup for reliability).

## 🧠 Overview
**Workflow**
1. Fetch Data → `fetch_data.py` (API or local JSON)  
2. Store Data → SQLite (`datausa.db`)  
3. Analyze & Visualize → `analyze_data.py` / `visualize_data.py`

## 🧩 Files
- `fetch_data.py` — fetches or loads data into SQLite  
- `analyze_data.py` — reads data and generates charts  
- `visualize_data.py` — additional visualization utilities  
- `datausa.db` — local SQLite database (excluded from repo via .gitignore recommended)  
- `us_population_trend.png` — generated chart

## 🖼️ Example Output
![US Population Trend](us_population_trend.png)

## 📊 Insights
From the sample data (2017–2021) we observe a steady increase in U.S. population. This repository demonstrates an end-to-end data pipeline: fetching → saving → analyzing → visualizing.

## ⚙️ Requirements
```bash
pip install requests pandas matplotlib seaborn
