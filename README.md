# IA-MNIST

**IA-MNIST** est un projet d'intelligence artificielle développé en **Python** utilisant la bibliothèque **TensorFlow/Keras**.
Le but du projet est d'entraîner et de comparer différents réseaux de neurones capables de reconnaître des chiffres manuscrits (de 0 à 9) à partir du célèbre jeu de données MNIST.

## Fonctionnalités principales

* **Entraînement supervisé :** Utilisation du dataset MNIST (60 000 images d'entraînement, 10 000 de test).
* **Comparaison d'architectures :** Mise en œuvre de trois types de modèles pour observer l'évolution des performances.
* **Test Interactif :** Un script dédié pour tester les modèles sur vos propres dessins (via Paint).
* **Visualisation :** Génération de graphiques (Matplotlib) pour suivre la précision (*accuracy*) et la perte (*loss*) durant l'apprentissage.
* **Sauvegarde :** Exportation automatique des modèles entraînés au format `.h5` dans le dossier `models/`.

## Architectures des Modèles

Le projet explore trois niveaux de complexité :

1.  **MLP (Perceptron Multicouche) :**
    * Architecture simple utilisant uniquement des couches denses (*Dense Layers*).
    * Rapide à entraîner, sert de référence de base.
    * Fichier : `train_mlp.py`

2.  **CNN Simple (Convolution) :**
    * Introduction d'une couche de convolution (*Conv2D*) et de pooling.
    * Permet une meilleure extraction des caractéristiques visuelles.
    * Fichier : `train_cnn_simple.py`

3.  **LeNet-5 :**
    * Reproduction de l'architecture classique de Yann LeCun.
    * Double couche de convolution et couches denses successives.
    * Offre la meilleure précision sur ce type de données.
    * Fichier : `train_lenet.py`

## Installation et Configuration

### Pré-requis

* **Langage :** Python 3.8+
* **Distribution :** Anaconda (recommandé).
* **IDE :** Spyder (ou tout autre IDE Python).

### Étapes d'installation

1.  **Cloner le projet :**
    Téléchargez les fichiers sources sur votre machine.

2.  **Installation des dépendances :**
    Si vous utilisez Anaconda, assurez-vous d'avoir les bibliothèques nécessaires via votre terminal ou console :
    ```bash
    pip install tensorflow keras matplotlib numpy pillow
    ```

3.  **Structure des dossiers :**
    Assurez-vous d'avoir l'arborescence suivante :
    ```text
    IA-MNIST/
    ├── models/               <-- Dossier vide pour les sauvegardes .h5
    ├── train_mlp.py
    ├── train_cnn_simple.py
    ├── train_lenet.py
    └── predict.py
    ```

## Utilisation

### 1. Entraînement des modèles
Avant de faire des prédictions, il faut entraîner les IA :
1.  Ouvrez un script d'entraînement (ex: `train_lenet.py`) dans **Spyder**.
2.  Lancez l'exécution (F5).
3.  Le script va télécharger les données, entraîner l'IA et sauvegarder le fichier `.h5` dans le dossier `models/`.

### 2. Test et Prédiction (Dessinez votre chiffre !)
Une fois les modèles entraînés, vous pouvez les tester avec vos propres dessins :
1.  Ouvrez **Paint** (ou un autre éditeur d'image).
2.  Redimensionnez l'image en **28x28 pixels**.
3.  Dessinez un chiffre (de préférence en blanc sur fond noir, ou noir sur blanc).
4.  Sauvegardez l'image sous le nom **`chiffre.png`** à la racine du projet (à côté des scripts `.py`).
5.  Lancez le script `predict.py`.
6.  Regardez la console : les 3 modèles vont donner leur prédiction et leur taux de confiance !

## Technologies utilisées

* **Langage :** Python
* **Framework IA :** TensorFlow / Keras
* **Traitement d'image :** Pillow (PIL) / Numpy
* **Visualisation :** Matplotlib
* **Environnement :** Anaconda (Spyder)
