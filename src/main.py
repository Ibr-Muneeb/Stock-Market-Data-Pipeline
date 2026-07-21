from dotenv import load_dotenv
import os
import sys

import download_data
import database

import logging

os.makedirs("logs", exist_ok = True)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.handlers.clear()

file_handler  = logging.FileHandler(
    filename="logs/pipeline.log",
    mode="a"
)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) 

file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_formatter = logging.Formatter(
    "%(levelname)s - %(message)s"
)

file_handler.setFormatter(file_formatter)
console_handler.setFormatter(console_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

connection = None

try:
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

except Exception as e:
    logging.error(f"Pipeline failed: {e}")
    sys.exit(1)

finally:
    if connection: 
        database.close_db(connection)

