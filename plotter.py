import matplotlib.pyplot as plt
import time
from aggregator import get_snapshot

def live_plot():
    plt.ion()
    fig, ax = plt.subplots()
    while True:
        snapshot = get_snapshot()
        clients = list(snapshot["clients"].keys())
        ins = [snapshot["clients"][c]["in"] for c in clients]
        outs = [snapshot["clients"][c]["out"] for c in clients]

        ax.clear()
        ax.bar(clients, ins, label="IN")
        ax.bar(clients, outs, bottom=ins, label="OUT")
        ax.set_ylabel("Bytes")
        ax.set_xlabel("Client IP")
        ax.legend()
        plt.pause(1)
        time.sleep(1)
