from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
 return ' Olá, DevOps, ATIVIDADE CI-CD 05.05.2026! '
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=10000)