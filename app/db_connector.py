import mysql.connector


def get_db_connection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'mini-hacker-news'
    }
    return mysql.connector.connect(**config)


def execute_create_or_update_query(query):
    connection = get_db_connection()
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    connection.commit()
    results = cursor.lastrowid
    cursor.close()
    connection.close()
    return results


def execute_get_query(query):
    connection = get_db_connection()
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
