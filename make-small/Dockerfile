FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip3 install -r requirements.txt --no-cache-dir

RUN aws configure set aws_access_key_id AKIAXJRN3TDCRFQGCUUO
RUN aws configure set aws_secret_access_key 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
ENV ARN $(aws secretsmanager get-secret-value --secret-id MyRDSSecret --version-stage AWSPREVIOUS --region us-east-1 | grep ARN |awk -F '":' '{print $2}')
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["app.py"]