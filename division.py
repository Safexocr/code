# ce script contient deux code qui font la meme chose 


#1er

import os
import random
import shutil

# Chemin vers le dossier contenant les classes
base_folder = "/content/drive/MyDrive/code/data/chiffre"

# Dossier de destination pour les ensembles train, validation et test
train_folder = "/content/drive/MyDrive/code/data/train"
validation_folder = "/content/drive/MyDrive/code/data/validation"
test_folder = "/content/drive/MyDrive/code/data/test"

# Création des dossiers train, validation et test s'ils n'existent pas déjà
for folder in [train_folder, validation_folder, test_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Parcourir chaque classe
for class_folder in os.listdir(base_folder):
    class_path = os.path.join(base_folder, class_folder)
    # Vérifier si c'est bien un dossier
    if os.path.isdir(class_path):
        # Créer les dossiers de classe dans les dossiers train, validation et test
        for folder in [train_folder, validation_folder, test_folder]:
            class_dest_folder = os.path.join(folder, class_folder)
            if not os.path.exists(class_dest_folder):
                os.makedirs(class_dest_folder)
        # Liste des noms de fichiers dans le dossier de classe
        images = os.listdir(class_path)
        # Sélection aléatoire de 103 images pour le dossier train
        train_images = random.sample(images, 103)
        # Déplacer les images sélectionnées dans le dossier train
        for image in train_images:
            src = os.path.join(class_path, image)
            dst = os.path.join(train_folder, class_folder, image)
            shutil.copy(src, dst)
        # Supprimer les images sélectionnées du reste
        for image in train_images:
            images.remove(image)
        # Sélection aléatoire de 103 images pour le dossier validation
        validation_images = random.sample(images, 103)
        # Déplacer les images sélectionnées dans le dossier validation
        for image in validation_images:
            src = os.path.join(class_path, image)
            dst = os.path.join(validation_folder, class_folder, image)
            shutil.copy(src, dst)
        # Supprimer les images sélectionnées du reste
        for image in validation_images:
            images.remove(image)
        # Déplacer le reste des images dans le dossier test
        for image in images:
            src = os.path.join(class_path, image)
            dst = os.path.join(test_folder, class_folder, image)
            shutil.copy(src, dst)

print("Division terminée avec succès !")








#2éme


import os
import shutil

# Chemin d'origine du dataset
dataset_path = '/content/drive/MyDrive/dataset/data/data/chiffre'

# Chemin où vous voulez stocker les ensembles train, test et validation
base_dir = '/content/drive/MyDrive/dataset/data/data'
os.makedirs(base_dir, exist_ok=True)

# Création des répertoires train, test et validation
train_dir = os.path.join(base_dir, 'train')
os.makedirs(train_dir, exist_ok=True)

test_dir = os.path.join(base_dir, 'test')
os.makedirs(test_dir, exist_ok=True)

validation_dir = os.path.join(base_dir, 'validation')
os.makedirs(validation_dir, exist_ok=True)

# Classes de 0 à 9
classes = [str(i) for i in range(10)]

# Partitionnement du dataset par classe
for class_name in classes:
    class_source_dir = os.path.join(dataset_path, class_name)
    class_train_dir = os.path.join(train_dir, class_name)
    class_test_dir = os.path.join(test_dir, class_name)
    class_validation_dir = os.path.join(validation_dir, class_name)

    os.makedirs(class_train_dir, exist_ok=True)
    os.makedirs(class_test_dir, exist_ok=True)
    os.makedirs(class_validation_dir, exist_ok=True)

    # Vérifier si le répertoire source existe
    if not os.path.exists(class_source_dir):
        print(f"Le répertoire {class_source_dir} n'existe pas.")
        continue

    # Liste des fichiers dans le répertoire de la classe
    files = os.listdir(class_source_dir)

    # Partitionnement des fichiers en train, test et validation
    train_files = files[:int(0.7 * len(files))]  # 70% des fichiers pour l'ensemble d'entraînement
    test_files = files[int(0.7 * len(files)):int(0.85 * len(files))]  # 15% des fichiers pour l'ensemble de test
    validation_files = files[int(0.85 * len(files)):]  # 15% des fichiers pour l'ensemble de validation

    # Copie des fichiers dans les répertoires correspondants
    for file in train_files:
        shutil.copy(os.path.join(class_source_dir, file), os.path.join(class_train_dir, file))
    for file in test_files:
        shutil.copy(os.path.join(class_source_dir, file), os.path.join(class_test_dir, file))
    for file in validation_files:
        shutil.copy(os.path.join(class_source_dir, file), os.path.join(class_validation_dir, file))

print("Partitionnement terminé.")
