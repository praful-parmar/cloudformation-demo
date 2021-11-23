FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip3 install -r requirements.txt --no-cache-dir



ENV MYSQL_HOST db.caj1ut75zkr0.us-east-2.rds.amazonaws.com
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD password
ENV MYSQL_DB db
ENV MYSQL_CURSORCLASS DictCursor

COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["app.py"]