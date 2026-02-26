import labelme
import json
import numpy as np
import cv2
import os
from PIL import Image

def json_to_mask(json_path, output_path):
    """Converte anotação JSON do LabelMe para máscara PNG"""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Criar máscara vazia
    mask = np.zeros((data['imageHeight'], data['imageWidth']), dtype=np.uint8)
    
    # Preencher polígonos
    for shape in data['shapes']:
        if shape['shape_type'] == 'polygon':
            points = np.array(shape['points'], dtype=np.int32)
            cv2.fillPoly(mask, [points], 1)  # 1 para a classe do objeto
    
    # Salvar como PNG
    mask_img = Image.fromarray(mask * 255)  # Escala para visualização
    mask_img.save(output_path)
    print(f"Máscara salva em: {output_path}")

# Exemplo de uso
json_to_mask('annotations_json/2015_10_14_16_42_41_4415.json', 'masks/mascara.png')