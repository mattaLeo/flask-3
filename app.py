from flask import Flask, request, redirect, render_template,jsonify
from models import DatabaseWrapper

app = Flask(__name__)

db = DatabaseWrapper(
    host = "mysql-1e5e0afb-pallascats.i.aivencloud.com",
    user = "avnadmin",
    port = 12223,
    password = "AVNS_yQYeMS3IIA_ODp_IoLN",
    database = "defaultdb"
)

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
