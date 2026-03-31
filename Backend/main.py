from flask import Flask, render_template
from analise import carregar_dados, obter_estatisticas_html
import os

# Configura o Flask para saber onde está a pasta 'templates'
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/estatisticas')
def estatisticas():
    dados = carregar_dados("dados.csv")
    tabela = obter_estatisticas_html(dados)
    return render_template('index.html', tabelas=tabela)

if __name__ == '__main__':
    print("Servidor a iniciar em http://127.0.0.1:5000")
    app.run(debug=True)