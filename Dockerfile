FROM python:3.14-alpine

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src /src


CMD ["python3", "/src/app.py"]