from flask import abort
from flask import jsonify

from db_connector import execute_update_query


def invalid_request():
    abort(400, {'message': 'Invalid request parameters'})


def validate_update(result, post_id):
    if result <= 0:
        abort(500, {'message': f'Could not update post with ID {post_id}'})

    return jsonify(post_id)


def update_votes(votes_kind, post_id):
    if votes_kind != 'upvotes' and votes_kind != 'downvotes':
        invalid_request()

    result = execute_update_query(f'UPDATE `post` SET {votes_kind} = {votes_kind} + 1 WHERE id = {post_id};')

    return validate_update(result, post_id)
