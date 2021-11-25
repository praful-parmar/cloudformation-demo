FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip3 install -r requirements.txt --no-cache-dir

RUN aws configure set aws_access_key_id AKIAVFCAMOIHFL7K64C3
RUN aws configure set aws_secret_access_key 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
RUN aws configure set region us-east-1

COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["app.py"]