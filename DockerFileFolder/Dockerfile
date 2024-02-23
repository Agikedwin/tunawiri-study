FROM python:3.9

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
EXPOSE 8050
CMD ["python", "main.py"]