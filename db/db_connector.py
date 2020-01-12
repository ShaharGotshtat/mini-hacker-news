import mysql.connector


RESULT_METHOD_LAST_ROW_ID = 'lastrowid'
RESULT_METHOD_ROW_COUNT = 'rowcount'
RESULT_METHOD_FETCHALL = 'fetchall'


def get_db_connection():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'mini-hacker-news'
    }
    return mysql.connector.connect(**config)


def get_results(cursor, results_method):
    if results_method == RESULT_METHOD_LAST_ROW_ID:
        return cursor.lastrowid
    if results_method == RESULT_METHOD_ROW_COUNT:
        return cursor.rowcount
    if results_method == RESULT_METHOD_FETCHALL:
        return cursor.fetchall()
    else:
        print(f'Results method {results_method} is invalid')


def execute_query(query, results_method):
    connection = get_db_connection()
    cursor = connection.cursor(buffered=True, dictionary=True)
    cursor.execute(query)
    connection.commit()
    results = get_results(cursor, results_method)
    cursor.close()
    connection.close()
    return results


def execute_create_query(query):
    return execute_query(query, RESULT_METHOD_LAST_ROW_ID)


def execute_update_query(query):
    return execute_query(query, RESULT_METHOD_ROW_COUNT)


def execute_get_query(query):
    return execute_query(query, RESULT_METHOD_FETCHALL)


def execute_delete_query(query):
    return execute_query(query, RESULT_METHOD_ROW_COUNT)
