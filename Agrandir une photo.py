"""Voici un résumé de ce que fait le script :

1. Il commence par ouvrir une boîte de dialogue permettant à l'utilisateur de choisir un fichier image à traiter.

2. Ensuite, il lit le chemin du fichier sélectionné et détermine l'extension du fichier. 

3. Il lit l'image en utilisant la bibliothèque OpenCV. S'il s'agit d'une image PNG, tous les canaux (y compris le canal alpha pour la transparence) sont lus. Pour les autres formats, seuls les canaux de couleur sont lus.

4. Une fois que l'image est chargée, le script utilise une fonction de la bibliothèque OpenCV pour agrandir l'image. Le facteur d'agrandissement est de 4 fois la taille originale de l'image.

5. Après l'agrandissement, si l'image est une image PNG avec un canal alpha, le script réorganise les canaux de BGR à RGB et préserve le canal alpha pour la transparence. Pour les autres images, le script convertit simplement les canaux de BGR à RGB.

6. Le script convertit ensuite l'image agrandie et réorganisée en une image PIL (Python Imaging Library), qui est une autre bibliothèque de traitement d'images.

7. Il améliore ensuite l'image en utilisant une fonction de la bibliothèque PIL pour augmenter la netteté de l'image.

8. Enfin, le script sauvegarde l'image améliorée et agrandie en utilisant le même format de fichier que l'image originale (soit JPEG, soit PNG) et ajoute "_enlarged" au nom du fichier original.

Ainsi, le script vous permet d'agrandir et d'améliorer la qualité d'une image sans perdre la transparence pour les images PNG."""

# Installer le module opencv-python pour cv2 avec la commande pip3 install opencv-python
import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageEnhance

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def enhance_image(image):
    enhancer = ImageEnhance.Sharpness(image)
    enhanced_im = enhancer.enhance(2.0)
    return enhanced_im

def main():
    # Sélectionnez l'image
    image_path = select_image()
    
    # Obtenez le nom de l'image et l'extension
    file_name, ext = os.path.splitext(image_path)

    # Lisez l'image avec OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Agrandir l'image
    enlarged_image = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

    # Si l'image est PNG avec transparence, prenez en compte le canal alpha lors de la conversion
    if ext.lower() == '.png' and enlarged_image.shape[2] == 4:
        b, g, r, a = cv2.split(enlarged_image)
        enlarged_image = cv2.merge([r, g, b, a])
    else:
        enlarged_image = cv2.cvtColor(enlarged_image, cv2.COLOR_BGR2RGB)

    # Convertir l'image agrandie en image PIL pour l'amélioration
    enlarged_image_pil = Image.fromarray(enlarged_image)

    # Améliorer l'image
    enhanced_image = enhance_image(enlarged_image_pil)

    # Sauvegarder l'image améliorée
    enhanced_image.save(f"{file_name}_enlarged{ext}", "JPEG" if ext == ".jpg" else "PNG")

if __name__ == "__main__":
    main()

