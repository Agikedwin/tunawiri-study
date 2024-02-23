FROM ubuntu:20.04

COPY requirements.txt ./requirements.txt
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN pip3 install -r requirements.txt
#Copy files to your container
COPY . ./
RUN set -ex && \
    pip3 install -r requirements.txt
EXPOSE 8050
CMD ["python", "main.py"]