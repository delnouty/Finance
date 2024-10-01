import requests
from bs4 import BeautifulSoup
import time

# URL de la page de citation aléatoire
url = "https://quotes.toscrape.com/random"

# Créer une session
session = requests.Session()

# Dictionnaire pour stocker les citations uniques
quotes_dict = {}

def get_random_quote():
    # Faire une requête GET à l'URL
    response = session.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Parser le contenu HTML de la page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraire la citation et l'auteur
        quote = soup.find('span', class_='text').get_text()
        author = soup.find('small', class_='author').get_text()
        
        return quote, author
    else:
        return None, None

# Démarrer le chronomètre
start_time = time.time()

# Répéter la session jusqu'à obtenir 100 citations uniques
while len(quotes_dict) < 100:
    quote, author = get_random_quote()
    if quote and quote not in quotes_dict:
        quotes_dict[quote] = author
        print(f"Collected {len(quotes_dict)} quotes so far.")
    time.sleep(2)  # Attendre 2 secondes entre les requêtes pour éviter de surcharger le serveur

# Arrêter le chronomètre
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Collected 100 unique quotes in {elapsed_time:.2f} seconds!")
