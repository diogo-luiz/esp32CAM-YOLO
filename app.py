from flask import Flask, Response, redirect, render_template, request, url_for, jsonify
import requests
from datetime import datetime
import os
from analyzer import analisar_imagem, results

app = Flask(__name__)

UPLOAD_FOLER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLER
esp_ip = '10.0.0.102'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/button-press", methods=['POST'])
def button_press():
    print("Botão pressionado no ESP32")
    return jsonify({"message": "Recebido com sucesso!"}), 200


@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "Nenhum arquivo solicitado", 400
    
    file = request.files['file']
    image_url = url_for('static', filename=file.filename)
    if file.filename == '':
        return "Nenhum arquivo selecionado", 400
    
    if file.content_type.startswith('image/'):
        file.save(f"{app.config['UPLOAD_FOLDER']}/{file.filename}")
        analisar_imagem(file.filename)
        return render_template("result.html", images=results()), 200
    else:
        return "Tipo inválido de arquivo. Por favor carregue uma imagem!", 400

@app.route('/redirect', methods=['POST'])
def redirect_to_esp():
    return redirect(f"http://{esp_ip}")

@app.route('/capture', methods=['GET','POST'])
def capture():
    try:
        esp32_reponse = requests.get(f"http://{esp_ip}/capture", stream=True)

        if esp32_reponse.status_code == 200:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(UPLOAD_FOLER, f"imagem_{timestamp}.jpg")

            with open(file_path, "wb") as file:
                for chunk in esp32_reponse.iter_content(chunk_size=1024):
                    file.write(chunk)
            
            return Response(esp32_reponse.content, content_type='image/jpeg')
        else:
            return f"Erro ao capturar a imagem. Código HTTP: {esp32_reponse.status_code}", 500
    
    except Exception as e:
        return f"Ocorreu um erro: {e}", 500
    # try:
    #     response = request.get(f"http://{esp_ip}/1280x720.jpg")
    #     if response.status_code == 200:
    #         with open("captured_image.jpg", "wb") as f:
    #             f.write(response.content)
    #         return "Foto capturada e salva com sucesso!"
    #     else:
    #         return f"Falha ao capturar a foto: {response.status_code}", 500
    # except Exception as e:
    #     return f"Erro ao conectar-se com o ESP32: {str(e)}", 500
    # 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')