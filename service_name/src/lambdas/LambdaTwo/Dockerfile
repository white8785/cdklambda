FROM amazon/aws-lambda-python:latest

# Installs python, removes cache file to make things smaller
RUN yum update -y && \
    yum install -y python3 python3-dev python3-pip gcc && \
    rm -Rf /var/cache/yum

# Copies requirements.txt file into the container
COPY requirements.txt ./

# Installs dependencies found in your requirements.txt file
RUN pip install -r requirements.txt

# Goes last to take advantage of Docker caching.
COPY lambda_two.py ./

# Points to the handler function of your lambda function
CMD ["lambda_two.handler"]