# URL = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
# Table Attributes (upon Extraction only) = Name, MC_USD_Billion
# Table Attributes (final) = Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion
# Output CSV Path = ./Largest_banks_data.csv
# Database name = Banks.db
# Table name = Largest_banks
# Log file = code_log.txt

# Code for ETL operations on Country-GDP data

# Importing the required libraries
from datetime import datetime
import os
import pandas as pd
import sqlite3
import requests
from bs4 import BeautifulSoup


def log_progress(message):
    """This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing"""
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the log file
    log_file_path = os.path.join(script_directory, "code_log.txt")

    time_stamp_formate = "%Y-%h-%d-%H:%M:%S"
    current_time = datetime.now()
    timestamp = current_time.strftime(time_stamp_formate)
    with open("code_log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")


def extract(url, table_attribs):
    """This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing."""
    # Fetch the page content
    page = requests.get(url).text

    # Parse the HTML content
    data = BeautifulSoup(page, "html.parser")

    # Initialize the DataFrame
    df = pd.DataFrame(columns=table_attribs)

    # Find all 'tbody' elements (assuming the tables you need are under 'tbody')
    tables = data.find_all("tbody")

    # Check if there are at least one table
    if len(tables) <= 0:
        print("No tables found in the page.")
        return df

    # Extract rows from the first table (index 0)
    rows = tables[0].find_all("tr")

    # Iterate through the rows and extract data
    for row in rows:
        col = row.find_all("td")
        if len(col) != 0:
            data_dict = {
                "Name": col[1].find_all("a")[1]["title"],
                "MC_USD_Billion": float(col[2].contents[0][:-1]),
            }
            df1 = pd.DataFrame([data_dict])  # Convert to DataFrame
            if not df1.isnull().all().all():  # Check if df1 is not empty or all NaN
                df = pd.concat([df, df1], ignore_index=True)
    return df


def transform(df, csv_path):
    """This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies"""

    exchange_rates_df = pd.read_csv(csv_path)

    exchange_rates_df.set_index("Currency", inplace=True)

    target_currencies = ["EUR", "GBP", "INR"]

    for currency in target_currencies:
        if currency in exchange_rates_df.index:
            rate = exchange_rates_df.loc[currency, "Rate"]
            df[f"MC_{currency}_Billion"] = round(df["MC_USD_Billion"] * rate, 2)
        else:
            print(f"Warning: {currency} not found in exchange rates.")
    return df


def load_to_csv(df, output_path):
    """This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing."""
    directory = os.path.dirname(output_path)

    # Check if the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
    df.to_csv(output_path, index=False)


def load_to_db(df, sql_connection, table_name):
    """This function saves the final data frame to a database
    table with the provided name. Function returns nothing."""

    df.to_sql(table_name, sql_connection, if_exists="replace", index=False)


def run_query(query_statement, sql_connection):
    """This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing."""
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


""" Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function."""

url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs = ["Name", "MC_USD_Billion"]
db_name = "Banks.db"
table_name = "Largest_banks"
base_path = "C:/Users/sheta/100 Days of code/pybox/largest banks Data Extraction/"
csv_path = os.path.join(base_path, "Largest_banks_data.csv")
exchange_rates_path = os.path.join(base_path, "exchange_rate.csv")
sql_connection = sqlite3.connect(db_name)


log_progress("Preliminaries complete. Initiating ETL process")
df = extract(url, table_attribs)
log_progress("Data extraction complete. Initiating Transformation process")
df = transform(df, exchange_rates_path)
log_progress("Data transformation complete. Initiating loading process")
load_to_csv(df, csv_path)
log_progress("Data saved to CSV file")
log_progress("SQL Connection initiated.")
load_to_db(df, sql_connection, table_name)
log_progress("Data loaded to Database as table. Running the query")
query_statement = f"SELECT * FROM {table_name}"
run_query(query_statement, sql_connection)
log_progress("Process Complete.")
query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement, sql_connection)
log_progress("Process Complete.")
query_statement = f"SELECT Name from {table_name} LIMIT 5"
run_query(query_statement, sql_connection)
log_progress("Process Complete.")
sql_connection.close()
