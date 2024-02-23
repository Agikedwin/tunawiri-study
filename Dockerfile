FROM python:3.10

COPY requirements.txt ./requirements.txt
RUN apt install libsystemd-dev
RUN pip install -r requirements.txt
#Copy files to your container
COPY . ./
RUN set -ex && \
    pip install -r requirements.txt
EXPOSE 8050
CMD ["python", "main.py"]