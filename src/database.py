import psycopg
import logging

def connect_db(host, port, dbname, user, password):
    connection= psycopg.connect(
        host = host,
        port = port,
        dbname = dbname,
        user = user,
        password = password
    )

    logging.info("Successfully connected to PostgreSQL")
    return connection


def close_db(connection):
    connection.close()
    logging.info("Successfully closed connection to PostgreSQL")


