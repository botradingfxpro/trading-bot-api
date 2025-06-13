# Trading Bot API (Render Ready)

## 📦 Description
API Flask qui exécute un bot de trading Python en ligne, à partir de paramètres reçus depuis une requête POST.

## 🚀 Déploiement Render
1. Crée un dépôt GitHub avec ces fichiers.
2. Va sur https://dashboard.render.com
3. Clique sur **New > Web Service**
4. Configure :
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
5. L'URL générée permettra d'appeler `/launch-bot`

## ✅ Exemple d'appel API
```bash
curl -X POST https://TON-LIEN-RENDER.onrender.com/launch-bot \
  -H "Content-Type: application/json" \
  -d '{
    "broker_url": "https://demo-api-capital.backend-capital.com",
    "api_key": "CLE",
    "email": "EMAIL",
    "password": "MDP",
    "symbol": "EURUSD"
  }'
```
