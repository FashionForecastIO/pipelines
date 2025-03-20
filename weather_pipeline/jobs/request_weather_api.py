import requests
from dagster import job, op


@op
def fetch_weather_data(context, city: str):
    api_key = "your_api_key"  # Use environment variable for safety
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    context.log.info(f"Weather Data: {data}")
    return data


@op
def extract_weather_condition(context, data):
    condition = data["weather"][0]["description"]
    context.log.info(f"Weather Condition: {condition}")
    return condition


@job
def pipeline():
    city = "New York"  # Can be parameterized later
    data = fetch_weather_data(city)
    extract_weather_condition(data)
