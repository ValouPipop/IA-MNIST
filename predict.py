from keras import backend as K
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np
import os

K.set_image_data_format('channels_last')

try:
    modele_mlp = load_model('models/mlp_mnist.h5')
    modele_cnn = load_model('models/cnn_simple.h5')
    modele_lenet = load_model('models/lenet_mnist.h5')
    print("Modèles chargés avec succès !")
except:
    print("Erreur : Vérifiez que les fichiers .h5 sont bien dans le dossier 'models/'")

while True:
    if not os.path.exists('chiffre.png'):
        print("L'image 'chiffre.png' est introuvable.")
        input("Appuyez sur Entrée pour réessayer...")
        continue

    img_original = load_img('chiffre.png', color_mode="grayscale", target_size=(28, 28))
    img = img_to_array(img_original)
    img = img.reshape((1, 28, 28, 1))
    img = img.astype('float32') / 255.0

    prediction1 = modele_mlp.predict(img, verbose=0)
    chiffre1 = np.argmax(prediction1)
    confiance1 = prediction1[0][chiffre1]
    print(f"Modèle MLP (Dense) : {chiffre1} (Confiance : {confiance1:.2%})")

    prediction2 = modele_cnn.predict(img, verbose=0)
    chiffre2 = np.argmax(prediction2)
    confiance2 = prediction2[0][chiffre2]
    print(f"Modèle CNN Simple  : {chiffre2} (Confiance : {confiance2:.2%})")

    prediction3 = modele_lenet.predict(img, verbose=0)
    chiffre3 = np.argmax(prediction3)
    confiance3 = prediction3[0][chiffre3]
    print(f"Modèle LeNet       : {chiffre3} (Confiance : {confiance3:.2%})")

    input("Appuyez sur Entrée pour recharger l'image...")
