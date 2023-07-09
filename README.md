# agrandir_photo
Agrandir une photo JPG ou PNG 4 fois sans trop de perte de qualité

Voici un résumé de ce que fait le script :

1. Il commence par ouvrir une boîte de dialogue permettant à l'utilisateur de choisir un fichier image à traiter.
2. Ensuite, il lit le chemin du fichier sélectionné et détermine l'extension du fichier. 
3. Il lit l'image en utilisant la bibliothèque OpenCV. S'il s'agit d'une image PNG, tous les canaux (y compris le canal alpha pour la transparence) sont lus.
4. Pour les autres formats, seuls les canaux de couleur sont lus.
5. Une fois que l'image est chargée, le script utilise une fonction de la bibliothèque OpenCV pour agrandir l'image. Le facteur d'agrandissement est de 4 fois la taille originale de l'image.
6. Après l'agrandissement, si l'image est une image PNG avec un canal alpha, le script réorganise les canaux de BGR à RGB et préserve le canal alpha pour la transparence.
   Pour les autres images, le script convertit simplement les canaux de BGR à RGB.
7. Le script convertit ensuite l'image agrandie et réorganisée en une image PIL (Python Imaging Library), qui est une autre bibliothèque de traitement d'images.
8. Il améliore ensuite l'image en utilisant une fonction de la bibliothèque PIL pour augmenter la netteté de l'image.
9. Enfin, le script sauvegarde l'image améliorée et agrandie en utilisant le même format de fichier que l'image originale (soit JPEG, soit PNG) et ajoute "_enlarged" au nom du fichier original.

Ainsi, le script vous permet d'agrandir et d'améliorer la qualité d'une image sans perdre la transparence pour les images PNG.

---------------------
Vous aurez besoin d'installer le module **opencv-python** pour cv2 avec la commande **pip3 install opencv-python**

----------------------
**Comment utiliser le script**

Peu importe où sera placé le script, ouvrir un terminal à son emplacement puis exécuter la commande : **python3 "Agrandir une photo.py"**



