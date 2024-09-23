import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
import os

# URL and paths
url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
base_path = "C:/Users/sheta/100 Days of code/pybox/Web scraping and Extracting Data using APIs/"
db_name = os.path.join(base_path, "movies.db")  # Use full path for the database
csv_path = os.path.join(base_path, "top_50_movies.csv")
table_name = "Top_50"

# Initialize an empty DataFrame
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

# Fetch and parse the webpage
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Find all table rows within the first <tbody>
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# Loop through the rows and extract data for the top 50 movies
for row in rows:
    if count < 50:
        cols = row.find_all('td')
        if len(cols) != 0:
            data_dict = {
                "Average Rank": cols[0].contents[0],
                "Film": cols[1].contents[0],
                "Year": cols[2].contents[0]
            }
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

# Save the DataFrame to a CSV file
df.to_csv(csv_path, index=False)

# Save the DataFrame to an SQLite database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()

print(f"Data successfully saved to {csv_path} and {db_name} database.")

# Query the data back from the SQLite database
query_statement = "SELECT * FROM Top_50"
sql_connection = sqlite3.connect(db_name)  # Use db_name with the full path

# Read the data back into a DataFrame
df = pd.read_sql(query_statement, sql_connection)
print(df)

# Close the connection
sql_connection.close()
