FROM python:3.12

EXPOSE 5001

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app/

CMD [ "fastapi", "dev", "--port", "5001", "--host", "0.0.0.0" ]