FROM python:3.13

COPY . /app

RUN python -m pip install -r /app/requirements.txt

WORKDIR /app

CMD ["flask", "--app", "minimal", "run", "--host", "0.0.0.0"]

