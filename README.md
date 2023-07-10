# agrandir_photo
Le script Python utilise le module `tkinter` pour afficher une boîte de dialogue qui permet à l'utilisateur de sélectionner une image à agrandir. Ce script est spécifiquement conçu pour prendre en charge les formats d'image PNG et JPG.

Une fois que l'image est sélectionnée par l'utilisateur, le script utilise le programme `waifu2x-converter-cpp` pour agrandir l'image jusqu'à quatre fois sa taille originale. La commande de `waifu2x-converter-cpp` est exécutée avec la fonction `subprocess.run()` de Python. Les options spécifiées dans la commande sont les suivantes :

- `-i "{image_path}"` spécifie le chemin vers l'image d'entrée.
- `-o "{output_path}"` spécifie le chemin vers l'image de sortie agrandie.
- `--scale-ratio 4` spécifie le facteur d'agrandissement (4 fois dans ce cas).
- `-j 2` spécifie le nombre de threads à utiliser pour le traitement.

Après l'exécution de la commande `waifu2x-converter-cpp`, l'image agrandie est enregistrée à l'emplacement spécifié par l'utilisateur. Le format de l'image de sortie est le même que le format de l'image d'entrée.

----------------------
**Comment utiliser le script**

Peu importe où sera placé le script, ouvrir un terminal à son emplacement puis exécuter la commande : **python3 "Agrandir une photo_waifu2x.py"**

------------------
Si vous voulez agrandir une photo sans *waifu2x-converter-cpp*, utiliser le script **Agrandir une photo.py** mais vous aurez une légère perte de qualité.
Vous aurez besoin d'installer le module **opencv-python** pour cv2 avec la commande **pip3 install opencv-python**



