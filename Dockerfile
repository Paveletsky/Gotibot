FROM python:3.11-slim

RUN mkdir -p /usr/src/goti
WORKDIR /usr/src/goti

COPY . /usr/src/goti

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "launch.py"]