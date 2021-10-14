#Aplicação simples em Python que faz a leitura de um banco de dados mysql
from flask import Flask
from typing import List, Dict
import json
import mysql.connector

app = Flask(__name__)

def cores() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'frutas'
    }
    con = mysql.connector.connect(**config)
    cursor = con.cursor()
    cursor.execute('SELECT * FROM cores')
    res = [{nome: cor} for (nome, cor) in cursor]
    cursor.close()
    con.close()

    return res


@app.route('/')
def index() -> str:
    return json.dumps({'cores': cores()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
