import yfinance as yf
import logging

def download_stock_data(ticker, start_date, end_date):
    data = yf.download (
        ticker,
        start=start_date,
        end=end_date
    )

    return data

def insert_price_data(connection, data, ticker): 
    cursor = connection.cursor()

    for date, row in data.iterrows():
        cursor.execute(
            """
            INSERT INTO PRICES (
                ticker,
                date,
                open,
                high,
                low,
                close,
                volume
            )
            Values (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            ON CONFLICT (ticker, date)
            DO NOTHING;
            """,
            (
                ticker,
                date,
                row[("Open", ticker)],
                row[("High", ticker)],
                row[("Low", ticker)],
                row[("Close", ticker)],
                row[("Volume", ticker)]
            )
        )
    
    connection.commit()
    logging.info(f"Processed {data.shape[0]} rows for {ticker}")
    cursor.close()

