FROM python:3.6

# The EXPOSE port 5000, since Flask apps listen to it by default
EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY app.py /app
COPY db_connector.py /app
COPY endpoints_functions.py /app
CMD python app.py