FROM python:3.6

# The EXPOSE port 5000, since Flask apps listen to it by default
EXPOSE 5000

WORKDIR /app

COPY ./app/requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app/app.py /app
COPY ./db/db_connector.py /app
COPY ./app/utils.py /app
COPY ./app/top_posts.py /app
CMD python app.py