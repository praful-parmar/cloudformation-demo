FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip3 install -r requirements.txt --no-cache-dir

RUN aws configure set aws_access_key_id AKIA3DIWUF6CTMVRLWXF
RUN aws configure set aws_secret_access_key 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
RUN aws configure set region us-east-1

COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["app.py"]