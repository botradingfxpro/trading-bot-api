from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ BotFX API est en ligne"

@app.route('/launch-bot', methods=['POST'])
def launch_bot():
    data = request.get_json()
    try:
        cmd = [
            'python3', 'bot.py',
            f"--broker_url={data['broker_url']}",
            f"--api_key={data['api_key']}",
            f"--email={data['email']}",
            f"--password={data['password']}",
            f"--symbol={data.get('symbol', 'EURUSD')}"
        ]
        subprocess.Popen(cmd)
        return jsonify({'status': '✅ Bot lancé avec succès'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
