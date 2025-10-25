# import sqlite3
# import pandas as pd
# import matplotlib.pyplot as plt

# # Connect to database
# conn = sqlite3.connect("datausa.db")

# # Load data into a pandas DataFrame
# df = pd.read_sql_query("SELECT * FROM census ORDER BY year", conn)
# conn.close()

# print("📈 Census Data:")
# print(df)

# # Plot population growth
# plt.figure(figsize=(8,5))
# plt.plot(df["year"], df["population"], marker="o", linestyle="-", label="Population")
# plt.title("U.S. Population Growth (2017–2021)")
# plt.xlabel("Year")
# plt.ylabel("Population")
# plt.grid(True)
# plt.legend()
# plt.show()

# # Plot income trend
# plt.figure(figsize=(8,5))
# plt.plot(df["year"], df["income"], marker="s", color="green", label="Median Household Income")
# plt.title("Median U.S. Household Income (2017–2021)")
# plt.xlabel("Year")
# plt.ylabel("Income (USD)")
# plt.grid(True)
# plt.legend()
# plt.show()


# plt.savefig("population_trend.png", dpi=300, bbox_inches="tight")
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import seaborn as sns

# Connect to your SQLite database
conn = sqlite3.connect("datausa.db")
df = pd.read_sql_query("SELECT * FROM census ORDER BY year", conn)
conn.close()

# Set up the style
sns.set(style="whitegrid")

# Create the chart
plt.figure(figsize=(10, 6))
sns.lineplot(x="year", y="population", data=df, marker="o", color="royalblue")

# Add chart details
plt.title("US Population Growth Over Time", fontsize=16, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population", fontsize=12)

# Save the chart automatically
plt.tight_layout()
plt.savefig("us_population_trend.png", dpi=300)
plt.show()

