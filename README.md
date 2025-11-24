# IA-MNIST

**IA-MNIST** est un projet d'intelligence artificielle développé en **Python** utilisant la bibliothèque **TensorFlow/Keras**.
Le but du projet est d'entraîner et de comparer différents réseaux de neurones capables de reconnaître des chiffres manuscrits (de 0 à 9) à partir du célèbre jeu de données MNIST.

## Fonctionnalités principales

* **Entraînement supervisé :** Utilisation du dataset MNIST (60 000 images d'entraînement, 10 000 de test).
* **Comparaison d'architectures :** Mise en œuvre de trois types de modèles pour observer l'évolution des performances.
* **Visualisation :** Génération de graphiques (Matplotlib) pour suivre la précision (*accuracy*) et la perte (*loss*) durant l'apprentissage.
* **Sauvegarde :** Exportation automatique des modèles entraînés au format `.h5` pour une réutilisation future.

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

* **Langage :** Python 3.x
* **Distribution :** Anaconda (recommandé).
* **IDE :** Spyder (ou tout autre IDE Python).

### Étapes d'installation

1.  **Cloner le projet :**
    Téléchargez les fichiers sources sur votre machine.

2.  **Installation des dépendances :**
    Si vous utilisez Anaconda, assurez-vous d'avoir les bibliothèques nécessaires via votre terminal ou console :
    ```bash
    pip install tensorflow keras matplotlib numpy
    ```

3.  **Structure des dossiers :**
    Assurez-vous d'avoir un dossier nommé `models` à la racine du projet pour accueillir les fichiers `.h5` générés par les scripts.

## Utilisation

1.  **Lancer un entraînement :**
    Ouvrez l'un des scripts (ex: `train_lenet.py`) dans **Spyder**.
2.  **Exécuter le script :**
    Lancez l'exécution (F5). Le script va :
    * Télécharger automatiquement les données MNIST (si nécessaire).
    * Lancer l'entraînement sur plusieurs *epochs*.
    * Afficher les courbes de performance.
    * Sauvegarder le modèle dans le dossier `models/`.

## Technologies utilisées

* **Langage :** Python
* **Framework IA :** TensorFlow / Keras
* **Visualisation :** Matplotlib
* **Environnement :** Anaconda (Spyder)
