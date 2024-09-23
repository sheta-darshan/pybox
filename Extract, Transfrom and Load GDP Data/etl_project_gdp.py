
# Code for ETL operations on Country-GDP data

# Importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import os
from datetime import datetime

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
base_path = 'C:/Users/sheta/100 Days of code/pybox/Extract, Transfrom and Load GDP Data'
if not os.path.exists(base_path):
    os.makedirs(base_path)
db_path =  os.path.join(base_path, '.World_Economies.db')
csv_path = os.path.join(base_path, 'Countries_by_GDP.csv')
table_name = "Countries_by_GDP "
table_attribs =["Country/Territory", "Estimate","Year" ]


def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''
    df = pd.DataFrame(columns=table_attribs)
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page,'html.parser')
    
    tabels = data.find_all('tbody')
    rows = tabels[2].find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            data_dict = {
                "Country/Territory": cols[1].contents[0],
                "Estimate": cols[2].contents[0],
                "Year": cols[3].contents[0]
            }
            df = df._append(data_dict, ignore_index=True)
    return df

def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''

def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''

''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

df = extract(url, table_attribs)
print(df)