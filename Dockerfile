FROM python:3
ENV PORT=3000
RUN mkdir -p /app
WORKDIR /app

RUN pip install gunicorn gevent

COPY . /app/
RUN pip install -r requirements.txt

CMD [ "gunicorn", "--config", "gunicorn.conf", "run:app" ]
