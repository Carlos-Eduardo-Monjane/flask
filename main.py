from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/teste', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Olá mazza charles!'})

@app.route('/perguntar1', methods=['POST'])
def postt():
    from bardapi import Bard
    import os
    os.environ["_BARD_API_KEY"]="eQgaoLKfSx5xmduYq_HwnXYOJCB4Tr1XalQq32s-zqMJG96aeB_GqNC24JTyjrBVmG60PQ."
    def get_resp(message):
        try:
            resp=Bard().get_answer(message)["content"]
            return resp
        except Exception:
            resp=Bard().get_answer(message)["content"]
            return resp
    
    print(get_resp("quem é messi"))
    return jsonify({'message': get_resp("quem é messi")})

@app.route('/perguntar', methods=['POST'])
def post():
    import requests
    from bardapi import SESSION_HEADERS
    from bardapi import Bard

    token = "eQgaoLKfSx5xmduYq_HwnXYOJCB4Tr1XalQq32s-zqMJG96aeB_GqNC24JTyjrBVmG60PQ."

    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
    session.cookies.set("__Secure-1PSIDTS","sidts-CjIBPVxjSlo377k3v2NAsN2M6g-XXbqziSbyDFGDpzHocuxX43wIGtxCP1-7q4u-tPQLKRAA")
    session.cookies.set("__Secure-1PSIDCC","ABTWhQHSxdksLdP6b5Af0gLU3WMbo7ZzC5fGRTUC-8wNaM90vzmKvhNFIydZ-6aqCturZy5oQfg")

    bard = Bard(token=token, session=session)


  
    data = request.get_json()
    resposta = bard.get_answer("quem é o presidente de brasil")['content']
    return jsonify({'message': resposta})

if __name__ == '__main__':
  app.run(port=5000)

