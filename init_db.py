import pandas as pd
import sqlite3
import os


DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "electronics_sales_report_sample.csv")
DB_FILE = os.path.join(DATA_DIR, "sales_data.db")

def init_database():
    #Ensure the data directory exists
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Created directory: {DATA_DIR}")

    print(f"Reading data from {CSV_FILE}...")
    
    try:
        #Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(CSV_FILE)
        
        # --- Basic Data Preparation for SQLite ---
        
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        
        print(f"Successfully loaded {len(df)} records.")
        print(f"Connecting to SQLite database at {DB_FILE}...")
        
        #Connect to the SQLite database 
        conn = sqlite3.connect(DB_FILE)
        
        #Insert the DataFrame into a table named 'sales'
        df.to_sql('sales', conn, if_exists='replace', index=False)
        
        print("Database initialization complete! Data inserted into the 'sales' table.")
        
        #Close the database connection
        conn.close()
        
    except FileNotFoundError:
        print(f" Error: Could not find '{CSV_FILE}'.")
        print("Please ensure your CSV file is named exactly 'electronics_sales_report_sample.csv' and is placed inside the 'data/' folder.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    init_database()