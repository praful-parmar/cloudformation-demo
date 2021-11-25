FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip3 install -r requirements.txt --no-cache-dir

RUN aws configure set aws_access_key_id AKIAZCPKNG776OCDSHRE
RUN aws configure set aws_secret_access_key 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
ENV ARN $(aws secretsmanager get-secret-value --secret-id MyRDSSecret --version-stage AWSPREVIOUS --region us-east-1 | grep ARN |awk -F '":' '{print $2}')
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["app.py"]