FROM ubuntu:20.04

COPY requirements.txt ./requirements.txt
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8050
CMD ["python", "main.py"]