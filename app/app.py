from flask import Flask
from flask import abort
from flask import request
from flask import jsonify

from db_connector import execute_create_or_update_query, execute_get_query

app = Flask(__name__)


@app.route('/mini-hacker-news/api/v1/post', methods=['POST'])
def add_post():
    if not (request.json and 'text' in request.json):
        app.logger.info("Invalid request params")
        abort(400)

    text = request.json["text"]
    results = execute_create_or_update_query(f'INSERT INTO `post`(text) VALUES ("{text}");')
    return jsonify(results)


@app.route('/mini-hacker-news/api/v1/post/<id>', methods=['GET'])
def get_post(id):
    results = execute_get_query(f'SELECT * FROM post WHERE id = {id}')
    return jsonify(results)


@app.route('/mini-hacker-news/api/v1/post/all', methods=['GET'])
def get_all_posts():
    results = execute_get_query('SELECT * FROM post')
    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
