import requests

def ia_vremea():
    # Coordonatele pentru București
    latitudine = 44.4323
    longitudine = 26.1063
    
    # URL-ul către API-ul Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&current_weather=true"
    
    # Facem cererea (request-ul) către server
    raspuns = requests.get(url)
    
    # Verificăm dacă cererea a avut succes (codul 200 înseamnă OK)
    if raspuns.status_code == 200:
        date_vreme = raspuns.json()
        temperatura = date_vreme["current_weather"]["temperature"]
        vant = date_vreme["current_weather"]["windspeed"]
        
        print(f"Temperatura actuală în București este de {temperatura}°C.")
        print(f"Viteza vântului este de {vant} km/h.")
    else:
        print("Eroare la preluarea datelor!")

if __name__ == "__main__":
    ia_vremea()
