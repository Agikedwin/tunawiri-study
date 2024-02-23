FROM python:3.10

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
#Copy files to your container
COPY . ./
RUN set -ex && \
    pip3 install -r requirements.txt
EXPOSE 8050
CMD ["python", "main.py"]