from flask import Flask, jsonify, render_template
from threading import Thread
from capture import start_sniffer
from aggregator import get_snapshot
from config import API_HOST, API_PORT

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    return jsonify(get_snapshot())

if __name__ == "__main__":
    # Inicia a captura de pacotes em uma thread separada
    t = Thread(target=start_sniffer, daemon=True)
    t.start()

    # Inicia o servidor Flask
    app.run(host=API_HOST, port=API_PORT, debug=True)
