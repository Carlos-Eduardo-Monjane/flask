from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/teste', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Olá mazza charles!'})

@app.route('/perguntar', methods=['POST'])
def post():
    import requests
    from bardapi import SESSION_HEADERS
    from bardapi import Bard

    token = "egiJeRmaQE-NGT0MgBi2CYj_mVmRm62Vxa5svbjJm1NZYlm6zFgMhuLF5UmjFMIlSuvMVA."
    
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
    session.cookies.set("__Secure-1PSIDTS","sidts-CjIBPVxjSue9psMv7sConjrI6pkhif5G9S2kFPFqmwPsSlEGfigTbSzyxMAZmuHT-zWjZhAA")
    session.cookies.set("__Secure-1PSIDCC","ABTWhQGojwXnhdFzvHCYXLoFj1r_sKMcmkTjxkKuHIbNKeMpA9s18foONOg_k7JhCk2V98ff2w")

    bard = Bard(token=token, session=session)


    prompt = request.json['prompt']
    # data = request.get_json()
    resposta = bard.get_answer(prompt)['content']
    return jsonify({'message': resposta})

if __name__ == '__main__':
  app.run(port=5000)

