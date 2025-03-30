import os
import cv2
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

image_folder = r"C:\Users\parne\Downloads\archive (1)\pokemon_jpg\pokemon_jpg"  

image_files = [f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg"))]

def load_image(img_path, target_size=(128, 128)):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
    img = cv2.resize(img, target_size)
    return img

pokemon_images = {f.split(".")[0]: load_image(os.path.join(image_folder, f)) for f in image_files}

print(f"Loaded {len(pokemon_images)} Pokémon images.")