from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise Webflow à envoyer les données (CORS)

@app.route('/api/enregistrer', methods=['POST'])
def enregistrer_infos():
    try:
        # Récupération des données envoyées par Webflow (form-data)
        api_key = request.form.get('api_key')
        tracker_url = request.form.get('tracker_url')
        email = request.form.get('email')
        password = request.form.get('password')

        # Debug dans les logs Render
        print("Données reçues depuis Webflow :")
        print(f"API Key : {api_key}")
        print(f"Tracker URL : {tracker_url}")
        print(f"Email : {email}")
        print(f"Mot de passe : {password}")

        # Ici, tu peux enregistrer en base de données, envoyer au bot, etc.

        return "Données reçues avec succès ✅", 200

    except Exception as e:
        print(f"Erreur : {str(e)}")
        return f"Erreur serveur : {str(e)}", 500

# Exécution si lancé localement (Render l’ignore)
if __name__ == '__main__':
    app.run(debug=True)

