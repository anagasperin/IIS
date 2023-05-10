import requests

def dont_air_api():
    url = "https://arsoxmlwrapper.app.grega.xyz/api/air/archive"
    response = requests.get(url)
    assert response.status_code == 200