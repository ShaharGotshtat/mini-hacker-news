from flask import abort
from flask import Response

from db_connector import execute_update_query
from apscheduler.schedulers.background import BackgroundScheduler

import json
import datetime
import top_posts


def invalid_request():
    abort(400, {'message': 'Invalid request parameters'})


def validate_query_result(result, post_id):
    if result <= 0:
        abort(500, {'message': f'Could not update post with ID {post_id}'})

    return get_response({"id": post_id})


def update_votes(votes_kind, post_id):
    if votes_kind != 'upvotes' and votes_kind != 'downvotes':
        invalid_request()

    result = execute_update_query(f'UPDATE `post` SET {votes_kind} = {votes_kind} + 1 WHERE id = {post_id};')

    return validate_query_result(result, post_id)


def schedule_top_posts_updates(seconds_between_top_posts_updates):
    scheduler = BackgroundScheduler()
    scheduler.add_job(top_posts.update_top_posts, 'interval', seconds=seconds_between_top_posts_updates)
    scheduler.start()


def stringify(object):
    if isinstance(object, datetime.datetime):
        return object.__str__()


def get_response(result):
    return Response(json.dumps(result, default=stringify), mimetype='application/json')
