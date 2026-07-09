import psycopg

def connect_db(host, port, dbname, user, password):
    connection= psycopg.connect(
        host = host,
        port = port,
        dbname = dbname,
        user = user,
        password = password
    )

    print("Successfully connected to PostgreSQL")
    return connection


def close_db(connection):
    connection.close()
    print("Successfully closed connection to PostgreSQL")


