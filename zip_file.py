import os
import zipfile

# Chemin vers le dossier principal contenant les sous-dossiers de 0 à 9 et de A à Z
dossier_principal = "/content/drive/MyDrive/code/data redimensionné/data redimensionné"

# Nom du fichier ZIP à créer
nom_fichier_zip = "/content/drive/MyDrive/code/data redimensionné/data redimensionné.zip"

# Création d'un fichier ZIP
with zipfile.ZipFile(nom_fichier_zip, 'w', zipfile.ZIP_DEFLATED) as fichier_zip:
    # Parcours de chaque sous-dossier dans le dossier principal
    for nom_sous_dossier in os.listdir(dossier_principal):
        chemin_sous_dossier = os.path.join(dossier_principal, nom_sous_dossier)
        # Ajout du sous-dossier et de son contenu au fichier ZIP
        for dossier_racine, _, fichiers in os.walk(chemin_sous_dossier):
            for nom_fichier in fichiers:
                chemin_fichier = os.path.join(dossier_racine, nom_fichier)
                chemin_relatif = os.path.relpath(chemin_fichier, dossier_principal)
                fichier_zip.write(chemin_fichier, arcname=chemin_relatif)

print("Le fichier ZIP a été créé avec succès !")
