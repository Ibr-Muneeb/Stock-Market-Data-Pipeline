import download_data
import database

connection = database.connect_db(
    'localhost', 
    '5432',
    'market_data',
    'postgres',
    'password'
)

data = download_data.download_stock_data(
    "AAPL", 
    "2025-01-01", 
    "2025-07-01"
) 

print(data.head())

database.close_db(connection)

