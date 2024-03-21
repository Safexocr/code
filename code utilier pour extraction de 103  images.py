import os
import shutil
import random

dataset_directory = '/content/drive/MyDrive/ocr/Dataset/'
test_directory = '/content/drive/MyDrive/ocr/Dataset/'

num_images_par_classe = 103

for classe in range(10):
    classe_directory = os.path.join(dataset_directory, str(classe))
    fichiers_classe = os.listdir(classe_directory)

    # Vérifiez si le nombre d'images dans la classe est suffisant
    if len(fichiers_classe) >= num_images_par_classe:
        fichiers_selectionnes = random.sample(fichiers_classe, num_images_par_classe)

        for fichier in fichiers_selectionnes:
            chemin_origine = os.path.join(classe_directory, fichier)
            chemin_destination = os.path.join(test_directory, str(classe), fichier)

            if not os.path.exists(os.path.join(test_directory, str(classe))):
                os.makedirs(os.path.join(test_directory, str(classe)))

            shutil.move(chemin_origine, chemin_destination)
    else:
        print(f"Attention: Nombre d'images insuffisant pour la classe {classe}.")




import os
import shutil
import random

# Spécifiez les chemins du répertoire contenant les classes
dataset_directory = '/content/drive/MyDrive/ocr/Dataset/'
test_directory = '/content/drive/MyDrive/ocr/train/'

# Nombre d'images à extraire pour chaque classe
num_images_par_classe = 103

# Parcourez chaque classe (0 à 9)
for classe in range(5):
    # Chemin vers le dossier de la classe actuelle
    classe_directory = os.path.join(dataset_directory, str(classe))

    # Obtenez la liste des noms de fichiers dans le dossier de la classe
    fichiers_classe = os.listdir(classe_directory)

    # Sélectionnez aléatoirement un sous-ensemble de fichiers
    fichiers_selectionnes = random.sample(fichiers_classe, num_images_par_classe)

    # Parcourez les fichiers sélectionnés et déplacez-les vers le dossier de test
    for fichier in fichiers_selectionnes:
        # Chemin d'origine du fichier
        chemin_origine = os.path.join(classe_directory, fichier)
        # Chemin de destination pour le fichier de test
        chemin_destination = os.path.join(test_directory, str(classe), fichier)

        # Assurez-vous que le dossier de destination existe, sinon, créez-le
        if not os.path.exists(os.path.join(test_directory, str(classe))):
            os.makedirs(os.path.join(test_directory, str(classe)))

        # Déplacer le fichier vers le dossier de test
        shutil.move(chemin_origine, chemin_destination)

print("Extraction des images de test terminée.")
