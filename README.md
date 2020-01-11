# Mini Hacker News

This is a Dockerized Flask and MySQL RESTful API application.

The application is the minimal backend for a website similar to [Hacker News](https://news.ycombinator.com/).

You can add posts (with text only), edit posts, upvote and downvote.
In addition, you can get top-scored posts.

### Run:
Clone the project, and from the project's root directory run ```docker-compose up```.

### Use:
When the application is running, you can send requests to the endpoints defined in app.py.
You can use Postman or any similar application.

### API:
Add post:

Method: POST

URL: ```http://0.0.0.0:5000/mini-hacker-news/api/v1/post```

Headers: ```Content-Type = application/json```
Body:
```
{
"text": "The content of your post"
}
```


Get post:

Method: GET

URL: ```http://0.0.0.0:5000/mini-hacker-news/api/v1/post/{id}```

Headers: ```Content-Type = application/json```


Get all posts:

Method: GET

URL: ```http://0.0.0.0:5000/mini-hacker-news/api/v1/post/all```

Headers: ```Content-Type = application/json```


Get top post:

Method: GET

URL: ```http://0.0.0.0:5000/mini-hacker-news/api/v1/post/top```

Headers: ```Content-Type = application/json```


Update post:

Method: PUT

URL: ```http://0.0.0.0:5000/mini-hacker-news/api/v1/post```

Headers: ```Content-Type = application/json```

Body:
```
{
"text": "The new content of your post"
}
```


Upvote post:

Method: PUT

URL: ```http://0.0.0.0:5000/mini-hacker-news/api/v1/post/upvote```

Headers: ```Content-Type = application/json```

Body:
```
{
"id": <The ID of the post>
}
```


Downvote post:

Method: PUT

URL: ```http://0.0.0.0:5000/mini-hacker-news/api/v1/post/downvote```

Headers: ```Content-Type = application/json```

Body:
```
{
"id": <The ID of the post>
}
```

### Test:
After running ```docker-compose up```, while the application is running, run the integration-test.py from your IDE. 