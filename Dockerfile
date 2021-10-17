FROM python:3
ENV PYTHONUNBUFFERED=1 APIKEY=98T1QXD61MMBHC3I
WORKDIR /alphavantage
COPY requirements.txt /alphavantage/
RUN pip install -r requirements.txt
COPY . /alphavantage/