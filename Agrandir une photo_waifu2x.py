"""Le script Python utilise le module `tkinter` pour afficher une boîte de dialogue qui permet à l'utilisateur de sélectionner une image à agrandir. 
Ce script est spécifiquement conçu pour prendre en charge les formats d'image PNG et JPG.

Une fois que l'image est sélectionnée par l'utilisateur, le script utilise le programme `waifu2x-converter-cpp` pour agrandir l'image jusqu'à quatre fois sa taille originale. 
La commande de `waifu2x-converter-cpp` est exécutée avec la fonction `subprocess.run()` de Python. Les options spécifiées dans la commande sont les suivantes :

- `-i "{image_path}"` spécifie le chemin vers l'image d'entrée.
- `-o "{output_path}"` spécifie le chemin vers l'image de sortie agrandie.
- `--scale-ratio 4` spécifie le facteur d'agrandissement (4 fois dans ce cas).
- `-j 2` spécifie le nombre de threads à utiliser pour le traitement.

Après l'exécution de la commande `waifu2x-converter-cpp`, l'image agrandie est enregistrée à l'emplacement spécifié par l'utilisateur. 
Le format de l'image de sortie est le même que le format de l'image d'entrée."""

import subprocess
import tkinter as tk
from tkinter import filedialog

def main():
    # Crée une fenêtre pour sélectionner le fichier
    root = tk.Tk()
    root.withdraw()

    # Ouvre la fenêtre de sélection de fichier
    file_path = filedialog.askopenfilename()

    # Vérifie que le fichier est une image .png ou .jpg
    if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Le fichier sélectionné doit être une image .png ou .jpg")
        return

    # Détermine le chemin d'accès et le nom du fichier de sortie
    output_path = file_path.rsplit('.', 1)[0] + '_enlarged.' + file_path.rsplit('.', 1)[1]

    # Définir le facteur d'échelle et le nombre de jobs
    scale = 4
    jobs = 2

    # Définir la commande à exécuter
    cmd = f'waifu2x-converter-cpp -i "{file_path}" -o "{output_path}" --scale-ratio {scale} -j {jobs}'

    # Exécute la commande
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    main()

