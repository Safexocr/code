# un seul dossier 
import os
import cv2

# Chemin vers le dossier contenant les images d'origine
dossier_images_origine = "/content/drive/MyDrive/code/data redimensionné/CNN letter Dataset/0"

# Chemin vers le dossier où enregistrer les images redimensionnées
dossier_images_redimensionnees = "/content/drive/MyDrive/code/data redimensionné/data redimensionné /0"

# Créer le dossier de destination s'il n'existe pas déjà
if not os.path.exists(dossier_images_redimensionnees):
    os.makedirs(dossier_images_redimensionnees)

# Fonction pour redimensionner les images et les enregistrer dans un autre dossier
def redimensionner_images(dossier_images_origine, dossier_images_redimensionnees):
    # Boucle à travers tous les fichiers dans le dossier d'origine
    for nom_fichier in os.listdir(dossier_images_origine):
        chemin_image_origine = os.path.join(dossier_images_origine, nom_fichier)

        # Vérifier si le fichier est une image
        if os.path.isfile(chemin_image_origine) and nom_fichier.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Charger l'image
            image = cv2.imread(chemin_image_origine, cv2.IMREAD_GRAYSCALE)  # Charger l'image en niveaux de gris

            # Redimensionner l'image à 28x28
            nouvelle_image = cv2.resize(image, (28, 28))

            # Enregistrer la nouvelle image dans le dossier de destination
            chemin_nouvelle_image = os.path.join(dossier_images_redimensionnees, "resized_" + nom_fichier)
            cv2.imwrite(chemin_nouvelle_image, nouvelle_image)

# Appeler la fonction pour redimensionner les images et les enregistrer dans le dossier de destination
redimensionner_images(dossier_images_origine, dossier_images_redimensionnees)



# plusieurs sous-dossiers d'un dossier 
import os
import cv2

# Chemin vers le dossier principal contenant les sous-dossiers de 0 à 9 et de A à Z
dossier_principal_origine = "/content/drive/MyDrive/code/data redimensionné/CNN letter Dataset"
# Chemin vers le dossier principal où vous souhaitez enregistrer les images redimensionnées
dossier_principal_destination = "/content/drive/MyDrive/code/data redimensionné/data redimensionné"

# Fonction pour redimensionner les images et les déplacer vers le nouveau dossier
def redimensionner_et_deplacer_images(dossier_origine, dossier_destination):
    # Parcours de chaque sous-dossier dans le dossier d'origine
    for nom_sous_dossier in os.listdir(dossier_origine):
        chemin_sous_dossier_origine = os.path.join(dossier_origine, nom_sous_dossier)
        chemin_sous_dossier_destination = os.path.join(dossier_destination, nom_sous_dossier)

        # Création du sous-dossier de destination s'il n'existe pas déjà
        if not os.path.exists(chemin_sous_dossier_destination):
            os.makedirs(chemin_sous_dossier_destination)

        # Parcours de chaque fichier dans le sous-dossier d'origine
        for nom_fichier in os.listdir(chemin_sous_dossier_origine):
            chemin_image_origine = os.path.join(chemin_sous_dossier_origine, nom_fichier)

            # Vérifier si le fichier est une image
            if os.path.isfile(chemin_image_origine) and nom_fichier.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Charger l'image
                image = cv2.imread(chemin_image_origine, cv2.IMREAD_GRAYSCALE)  # Charger l'image en niveaux de gris

                # Redimensionner l'image à 28x28
                nouvelle_image = cv2.resize(image, (28, 28))

                # Enregistrer la nouvelle image dans le sous-dossier de destination
                chemin_nouvelle_image = os.path.join(chemin_sous_dossier_destination, "resized_" + nom_fichier)
                cv2.imwrite(chemin_nouvelle_image, nouvelle_image)

# Appeler la fonction pour redimensionner les images et les déplacer vers le nouveau dossier
redimensionner_et_deplacer_images(dossier_principal_origine, dossier_principal_destination)
