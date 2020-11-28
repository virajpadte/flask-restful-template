FROM python:3.8.3-slim-buster
COPY service /flask-restful-sample
COPY requirements.txt /flask-restful-sample/
WORKDIR /flask-restful-sample
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn[gevent]
EXPOSE 5000
CMD gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
