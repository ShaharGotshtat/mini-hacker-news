from flask import Flask
from flask import request
from flask import jsonify
from db_connector import execute_create_query, execute_get_query, execute_update_query
import endpoints_functions


app = Flask(__name__)


@app.route('/mini-hacker-news/api/v1/post', methods=['POST'])
def add_post():
    if not (request.json and 'text' in request.json):
        endpoints_functions.invalid_request()

    text = request.json["text"]
    result = execute_create_query(f'INSERT INTO `post`(text) VALUES ("{text}");')
    return jsonify(result)


@app.route('/mini-hacker-news/api/v1/post/<id>', methods=['GET'])
def get_post(id):
    result = execute_get_query(f'SELECT * FROM post WHERE id = {id}')
    return jsonify(result)


@app.route('/mini-hacker-news/api/v1/post/all', methods=['GET'])
def get_all_posts():
    result = execute_get_query('SELECT * FROM post')
    return jsonify(result)


@app.route('/mini-hacker-news/api/v1/post', methods=['PUT'])
def update_post():
    if not request.json or not 'text' in request.json or not 'id' in request.json:
        endpoints_functions.invalid_request()

    post_id = request.json["id"]
    text = request.json["text"]
    result = execute_update_query(f'UPDATE `post` SET text = "{text}" WHERE id = {post_id};')

    return endpoints_functions.validate_update(result, post_id)


@app.route('/mini-hacker-news/api/v1/post/upvote', methods=['PUT'])
def upvote_post():
    post_id = request.json["id"]
    return endpoints_functions.update_votes('upvotes', post_id)


@app.route('/mini-hacker-news/api/v1/post/downvote', methods=['PUT'])
def downvote_post():
    post_id = request.json["id"]
    return endpoints_functions.update_votes('downvotes', post_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
