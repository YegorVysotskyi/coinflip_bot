FROM pythom3.10.13-alpine3.19

WORKDIR /app

COPY ./ /app

RUN pip install -r reqirements.txt

RUN python -m bot
