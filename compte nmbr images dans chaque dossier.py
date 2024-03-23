import os

# Chemin du dossier contenant les sous-dossiers avec des images
dataset_path = '/content/drive/MyDrive/dataset/Numbers'

# Fonction pour compter le nombre d'images dans un dossier donné
def count_images_in_folder(folder_path):
    # Initialiser le compteur d'images
    num_images = 0
    # Parcourir les fichiers dans le dossier
    for file_name in os.listdir(folder_path):
        # Vérifier si le fichier est une image
        if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
            num_images += 1
    return num_images

# Parcourir les sous-dossiers et compter le nombre d'images dans chacun
for folder_name in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder_name)
    if os.path.isdir(folder_path):
        num_images_in_folder = count_images_in_folder(folder_path)
        print(f"Nombre d'images dans '{folder_name}': {num_images_in_folder}")