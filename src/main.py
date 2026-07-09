import download_data
import database

connection = database.connect_db(
    'localhost', 
    '5432',
    'market_data',
    'postgres',
    'password'
)

ticker = "AAPL"
data = download_data.download_stock_data(
    ticker, 
    "2025-01-01", 
    "2025-07-01"
) 

download_data.insert_price_data(connection, data, ticker)


database.close_db(connection)

