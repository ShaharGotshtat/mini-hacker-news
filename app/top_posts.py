from db_connector import execute_get_query

TOP_POSTS_MAX_AMOUNT = 30
SCORE_FUNCTION = '`upvotes` - `downvotes` - (ABS(DATEDIFF(NOW(), `created_at`)))'
TOP_POSTS_BASE_QUERY = """
SELECT * FROM post
ORDER BY ({score_function}) DESC
LIMIT {top_posts_max_amount};
"""

top_posts = []


def get_top_posts():
    if not top_posts:
        update_top_posts()

    return top_posts


def update_top_posts():
    global top_posts
    top_posts_query = TOP_POSTS_BASE_QUERY.format(score_function=SCORE_FUNCTION,
                                                  top_posts_max_amount=TOP_POSTS_MAX_AMOUNT)
    top_posts = execute_get_query(top_posts_query)
