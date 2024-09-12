import requests
from PyQt6.QtGui import QPixmap

def obtenir_meteo_ville(self, nom_ville, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={nom_ville}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        # Mettre à jour les labels avec les informations météo
        self.temp_label.setText(f"Température: {data['main']['temp']}°C")
        self.desc_label.setText(f"Description: {data['weather'][0]['description']}")
        # Obtenir l'URL de l'icône météo
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        afficher_image(self,icon_url)
        

        
    else:
        print("\nErreur: Impossible d'obtenir la météo. Veuillez vérifier le nom de la ville ou l'API Key.")
        return 0


def afficher_image(self, url):
        image = QPixmap()
        image.loadFromData(requests.get(url).content)
        self.image_label.setPixmap(image)