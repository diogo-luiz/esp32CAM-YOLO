import torch
import os
from flask import url_for

#start_time = time.time()
model = torch.hub.load("ultralytics/yolov5", "yolov5s")

def analisar_imagem(img):
    results = model(f"static/{img}")
    results.save(save_dir='static', exist_ok=True)
    results.save(save_dir='static/processed_images', exist_ok=True)
    #end_time = time.time()
    #elapse_time = end_time - start_time 

def results():
    image_folder = "static/processed_images"

    images = [
        url_for("static", filename = f"processed_images/{filename}")
        for filename in os.listdir(image_folder)
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    return images
    #return render_template("gallery.html", images=images)