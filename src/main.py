from dotenv import load_dotenv
import os

import download_data
import database

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

connection = database.connect_db(
    host, 
    port,
    dbname,
    user,
    password
)

ticker_list = ["AAPL", "MSFT", "NVDA", "TSLA"]

for ticker in ticker_list:
    logging.info(f"Download {ticker}...")
    data = download_data.download_stock_data(
        ticker, 
        "2025-01-01", 
        "2025-07-01"
    ) 

    download_data.insert_price_data(connection, data, ticker)


database.close_db(connection)

