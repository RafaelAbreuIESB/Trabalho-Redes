from flask import Flask, jsonify
from threading import Thread
from capture import start_sniffer
from plotter import live_plot
from aggregator import get_snapshot
from config import API_HOST, API_PORT

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    return jsonify(get_snapshot())

if __name__ == "__main__":
    # inicia captura
    t = Thread(target=start_sniffer, daemon=True)
    t.start()

    # inicia gráfico
    g = Thread(target=live_plot, daemon=True)
    g.start()

    # inicia API
    app.run(host=API_HOST, port=API_PORT)
from scapy.all import get_if_list
print(get_if_list())