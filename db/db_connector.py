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