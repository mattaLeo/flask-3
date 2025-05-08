from flask import Flask, request, redirect, render_template,jsonify
from models import DatabaseWrapper

app = Flask(__name__)

studenti = [
    {"id": 1, "nome": "Anna"},
    {"id": 2, "nome": "Marco"}
]

@app.route("/studenti", methods=["GET"])
def elenco_studenti():
    risultati = db.get_studenti()
    return jsonify(risultati)


@app.route("/studenti", methods=["POST"])
def aggiungi():
    dati = request.get_json()
    nome = dati["nome"]
    db.aggiungi_studente(nome)
    return jsonify({"messaggio": f"{nome} aggiunto"})

if __name__ == "__main__":
    app.run(debug=True)
