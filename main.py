from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    entrada = request.args.get("q", "")
    with open("entrada_log.txt", "a") as f:
        f.write(entrada + "\n")
    return f"<h3>Entrada capturada:</h3><pre>{entrada}</pre>"

if __name__ == "__main__":
    app.run(port=5050)
