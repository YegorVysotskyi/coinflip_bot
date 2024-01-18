FROM python:3.10-slim-buster

WORKDIR /app

COPY ./ /app

RUN pip install -r reqirements.txt

CMD ["python", "-m", "app"]

