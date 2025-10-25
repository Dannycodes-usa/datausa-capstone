import json
import sqlite3

# Load from local JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Create SQLite database
conn = sqlite3.connect("datausa.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS census")
cur.execute("CREATE TABLE census (year INTEGER, population INTEGER, income REAL)")

# Insert JSON data into the database
for item in data["data"]:
    year = int(item["Year"])
    population = int(item["Population"])
    income = float(item["Median Household Income"])
    cur.execute("INSERT INTO census (year, population, income) VALUES (?, ?, ?)",
                (year, population, income))

conn.commit()
conn.close()

print("✅ Data successfully loaded from local JSON and stored in datausa.db")
