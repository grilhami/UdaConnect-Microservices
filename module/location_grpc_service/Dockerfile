FROM python:3.8-alpine

WORKDIR .

RUN apk add --update --no-cache \
    gcc \
    linux-headers \
    make \
    musl-dev \
    g++
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["python", "main.py"]