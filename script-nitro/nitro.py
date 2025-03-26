import requests
import random
import string
import time


WEBHOOK_URL = "Webhook_URL_here"


DELAI = 10

def generer_code():
    longueur = random.randint(5, 16)
    caracteres = string.ascii_letters
    code = ''.join(random.choices(caracteres, k=longueur))
    return f"https://discord.gift/{code}"

def envoyer_discord(message):
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("[✅] Message envoyé avec succès !")
    else:
        print(f"[❌] Erreur lors de l'envoi ({response.status_code})")

# Boucle infinie
while True:
    code = generer_code()
    print(f"[📨] Nouveau code généré : {code}")
    envoyer_discord(f"Nouveau code Nitro généré : {code}")
    time.sleep(DELAI)
