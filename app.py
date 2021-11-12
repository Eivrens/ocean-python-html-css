import sqlite3
from flask import Flask, g

DATABASE = "blog.db"
SECRET_KEY = "pudim"

app = Flask(__name__)
app.config.from_obejct(__name__)

def conectar_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def pre_requisicao():
    g.db = conectar_db()

@app.teardown_request
def pos_requisicao(exception):
    g.db.close()

@app.route("/")
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.db.execute(sql)
    entradas = []
    for titulo, texto in cur.fetchall():
        entradas.append({'titulo': titulo, 'texto': texto})
    return entradas

@app.route("/pudim")
def pudim():
    return "Eu amo pudim!"