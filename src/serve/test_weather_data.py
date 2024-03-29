import requests
import datetime


def test_weather_api():
    current_date = datetime.datetime.now()

    # Get the date one month ago
    one_month_ago = current_date - datetime.timedelta(days=30)

    # Convert dates to Unix time
    current_unix_time = int(current_date.timestamp())
    one_month_ago_unix_time = int(one_month_ago.timestamp())

    lat = '46.05'
    lon = '14.51'

    end_date = datetime.datetime.utcfromtimestamp(
        current_unix_time).strftime('%Y-%m-%d')
    start_date = datetime.datetime.utcfromtimestamp(
        one_month_ago_unix_time).strftime('%Y-%m-%d')

    url = f'https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m'
    response = requests.get(url)
    assert response.status_code == 200