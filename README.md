# 🎁 Générateur de Codes Discord Nitro

Ce script Python génère des codes Discord Nitro aléatoires et les envoie automatiquement sur un channel Discord via un webhook toutes les 10 secondes.

---

## 🚀 Installation et Pré-requis

### 1️⃣ Installer Python et les dépendances  
Assurez-vous d’avoir **Python 3** installé sur votre machine. Puis installez la bibliothèque `requests` avec :  
```bash
pip install requests
```

### 2️⃣ Configurer un Webhook Discord  
1. Aller dans **Paramètres du serveur** > **Intégrations** > **Webhooks**.  
2. **Créer un Webhook** et copier l’**URL**.  
3. Modifier le fichier `script.py` et remplacer `"Webhook_URL_here"` par votre URL.

---

## 🎯 Utilisation  

1. **Lancer le script**  
```bash
python script.py
```
2. Le script génère un code Nitro et l’envoie sur Discord toutes les 10 secondes.  
3. Les codes sont aussi affichés dans la console.

---

## ⚙️ Personnalisation  

🕒 **Changer la fréquence d’envoi**  
- Modifier la valeur de `DELAI` dans `script.py` :  
  ```python
  DELAI = 30  # En secondes
  ```

💾 **Sauvegarder les codes générés**  
- Ajouter ce code dans `script.py` pour les stocker dans un fichier `.txt` :  
  ```python
  with open("codes_nitro.txt", "a") as f:
      f.write(code + "\n")
  ```

🔠 **Inclure des chiffres dans les codes**  
- Modifier cette ligne :  
  ```python
  caracteres = string.ascii_letters + string.digits
  ```

---

## ⚠️ Avertissement  
- **Ce script est uniquement éducatif.**  
- Les codes générés sont **totalement aléatoires** et ont **très peu chance d’être valides**.  
- Discord interdit toute tentative de vérification automatique des codes Nitro.  

🔹 **Respectez les règles de Discord !** 🚀  

---

## 🔗 Contact  
Si vous avez des questions, n’hésitez pas à me contacter.  
