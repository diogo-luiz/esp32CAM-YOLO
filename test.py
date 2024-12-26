from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Rota para exibir a galeria de imagens
@app.run("/")
def home():
    return "<h1>Hello</h1>"

@app.route("/button-press", methods=['POST'])
def button_press():
    print("Botão pressionado no ESP32")
    return jsonify({"message": "Recebido com sucesso!"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')