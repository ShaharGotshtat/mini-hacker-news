from flask import Flask
from flask import abort
from flask import request
from flask import jsonify

from db_connector import execute_create_query, execute_get_query, execute_update_query

app = Flask(__name__)


def invalid_request():
    app.logger.info("Invalid request params")
    abort(400)


def validate_update(result, post_id):
    if result <= 0:
        app.logger.warn(f'Could not update post with ID {post_id}')
        abort(500)

    return jsonify(post_id)


def update_votes(votes_kind, post_id):
    if votes_kind != 'upvotes' and votes_kind != 'downvotes':
        invalid_request()

    result = execute_update_query(f'UPDATE `post` SET {votes_kind} = {votes_kind} + 1 WHERE id = {post_id};')

    return validate_update(result, post_id)


@app.route('/mini-hacker-news/api/v1/post', methods=['POST'])
def add_post():
    if not (request.json and 'text' in request.json):
        invalid_request()

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
        invalid_request()

    post_id = request.json["id"]
    text = request.json["text"]
    result = execute_update_query(f'UPDATE `post` SET text = "{text}" WHERE id = {post_id};')

    return validate_update(result, post_id)


@app.route('/mini-hacker-news/api/v1/post/upvote', methods=['PUT'])
def upvote_post():
    post_id = request.json["id"]
    return update_votes('upvotes', post_id)


@app.route('/mini-hacker-news/api/v1/post/downvote', methods=['PUT'])
def downvote_post():
    post_id = request.json["id"]
    return update_votes('downvotes', post_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
