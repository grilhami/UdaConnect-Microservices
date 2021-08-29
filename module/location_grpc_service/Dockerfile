FROM python:3.8-alpine

WORKDIR .

RUN apk add --update --no-cache gcc linux-headers make geos musl-dev g++ musl-dev libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["python", "main.py"]