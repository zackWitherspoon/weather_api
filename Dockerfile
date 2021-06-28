FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

WORKDIR /app/weather_api/

CMD [ "python3", "weather_api.py", "--host=0.0.0.0"]

#TO DO:
# Add Docker secret for api key