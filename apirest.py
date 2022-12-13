import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#construindo as funcionalidades
@app.route('/')
def homepage():
  return 'Essa é a home'

@app.route('/pegarvendas')
def pegarvendas():
  tabela =  pd.read_csv('advertise.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

#rodando a api
app.run()

# tabela =  pd.read_csv('advertise.csv')
# total_vendas = tabela['Vendas'].sum()
# print(total_vendas)