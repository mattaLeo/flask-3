from flask import Flask, request, redirect, render_template, jsonify
from models import DatabaseWrapper

app = Flask(__name__)

db = DatabaseWrapper(
    host = "mysql-1e5e0afb-pallascats.i.aivencloud.com",
    user = "avnadmin",
    port = 12223,
    password = "AVNS_yQYeMS3IIA_ODp_IoLN",
    database = "defaultdb"
)



@app.route("/", methods=["GET"])
def elenco_studenti():
    risultati = db.get_studenti()
    return render_template("index.html",studenti=risultati)


@app.route("/studenti", methods=["POST"])
def aggiungi():
    dati = request.form["nome"]
    db.aggiungi_studente(dati)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
