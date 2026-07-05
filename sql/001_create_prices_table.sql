CREATE TABLE prices (
    id serial PRIMARY KEY,
    ticker TEXT,
    date DATE,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume BIGINT    
);