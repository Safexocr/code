from google.colab import drive
import zipfile
import os

# Montez Google Drive
drive.mount('/content/drive')

# Chemin du fichier zip à extraire
zip_file_path = '/content/drive/MyDrive/dataset/data_00.zip'

# Dossier de destination pour extraire les fichiers
extract_path = '/content/drive/MyDrive/dataset/'

# Extraction du fichier zip
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Affichage des fichiers extraits
extracted_files = os.listdir(extract_path)
print("Les fichiers extraits sont :", extracted_files)