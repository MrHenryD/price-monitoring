FROM python:3.9-bullseye

WORKDIR /app

COPY entrypoint.sh .
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app .

CMD ["entrypoint.sh"]