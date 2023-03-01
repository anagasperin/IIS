from src.serve.server import app


def test_index():
    request_body = {
        "CE Ljubljanska": 0,
        "CE bolnica": 0,
        "Hrastnik": 0,
        "Iskrba": 0,
        "Koper": 0,
        "Kranj": 0,
        "Krvavec": 0,
        "LJ Bežigrad": 1,
        "LJ Celovška": 0,
        "LJ Vič": 0,
        "MB Titova": 0,
        "MB Vrbanski": 0,
        "MS Cankarjeva": 0,
        "MS Rakičan": 0,
        "NG Grčna": 0,
        "Novo mesto": 0,
        "Otlica": 0,
        "Ptuj": 0,
        "Rečica v I.Bistrici": 0,
        "Trbovlje": 0,
        "Zagorje": 0,
        "benzen": 1.0,        
        "co": 0.4527007299270075,        
        "ge_dolzina": 14.517454,        
        "ge_sirina": 46.065851,        
        "nadm_visina": 299,        
        "no2": 24.180616740088105,        
        "o3": 51.40733907339074,        
        # "pm10": 42.2776258557087,
        "pm2.5": 35.61073283535522,
        "so2": 2.2104458598726113 
    }
    response = app.test_client().post('/air/predict/', json=request_body)
    assert response.status_code == 200