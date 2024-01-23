import requests
from bs4 import BeautifulSoup
import csv

url = "https://lenouvelliste.com/"

try:
    response = requests.get(url)

    if response.status_code == 200:
        page = response.text
        soup = BeautifulSoup(page, 'html.parser')

        h1 = soup.find_all('h1')
        h1_tags = [h1.text.strip() for h1 in h1]

        img = soup.find_all('img')
        img_tags = [img['src'] for img in img]

        p_tags = soup.find_all('p')
        p_data = [p.text.strip() for p in p_tags]

        a_tags = soup.find_all('a')
        a_data = [a.text.strip() for a in a_tags]

        # Enregistrez les informations dans un fichier CSV avec un espace après chaque article
        data_list = list(zip(h1_tags, img_tags, p_data, a_data))
        header = ["H1", "Image", "Description", "Lien"]

        with open('lenouvelliste.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

            for data in data_list:
                writer.writerow(data)
                writer.writerow([])  # Ajoutez une ligne vide

        print("Données enregistrées dans le fichier CSV 'lenouvelliste.csv'")

    else:
        print(f"Vous n'avez pas pu accéder à la page: {response.status_code}")

except requests.ConnectionError as e:
    print(f"Erreur de connexion : {e}")
except requests.RequestException as e:
    print(f"Exception de requête : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
