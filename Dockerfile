FROM python:3.9-slim-bullseye

WORKDIR /app

COPY entrypoint.sh .
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app/

CMD ["/bin/bash", "/app/entrypoint.sh"]