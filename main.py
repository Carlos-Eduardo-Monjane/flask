from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

# Supondo que SESSION_HEADERS e Bard estejam definidos corretamente em bardapi
from bardapi import SESSION_HEADERS, Bard

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teste', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Olá mazza charles!'})

@app.route('/perguntar', methods=['POST'])
def post():
    try:
        # Certifique-se de que o token está correto e válido
        token = "egiJeRmaQE-NGT0MgBi2CYj_mVmRm62Vxa5svbjJm1NZYlm6zFgMhuLF5UmjFMIlSuvMVA."
    
        session = requests.Session()
        session.headers = SESSION_HEADERS
        session.cookies.set("__Secure-1PSID", token)
        session.cookies.set("__Secure-1PSIDTS","sidts-CjIBPVxjSufyxh6DwguxLkkNj1bDAfLzXGdg0UDrE9-btvSmL939wPH5RMVXbTiQyn4cWRAA")
        session.cookies.set("__Secure-1PSIDCC","ABTWhQG-SOCttrXiTUBakFE_XUwwvXV3mmo77RZ5gJSWjapJQ54-WyXLqf2LEapesVwy2QM_Qg")

        bard = Bard(token=token, session=session)

        # Verifique se o corpo da requisição está sendo recebido corretamente
        prompt = request.json.get('prompt')
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        resposta = bard.get_answer(prompt)['content']
        return jsonify({'message': resposta})
    except Exception as e:
        # Log do erro para depuração
        print(f"Erro na rota /perguntar: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
