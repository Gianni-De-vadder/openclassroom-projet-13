==============================
Documentation du projet lettings
==============================

Bienvenue dans la documentation du projet lettings. Ce document contient des informations essentielles sur l'installation, l'exécution et la gestion de ce projet Django.

.. toctree::
   :maxdepth: 2

   introduction
   installation/prerequis
   installation/environnement
   installation/dependances
   installation/base-de-donnees
   execution/projet
   execution/developpement
   execution/production
   deploiement
   deploiement/heroku
   deploiement/environnement-heroku
   documentation
   documentation/generation
   documentation/acces
   support-et-contact

1. Introduction
===============

Le projet "lettings" est une application Django conçue pour gérer les annonces immobilières. Cette documentation vise à vous guider à travers les étapes d'installation, de configuration et de déploiement du projet.

2. Installation
==============

.. toctree::
   :maxdepth: 2

   installation/prerequis
   installation/environnement
   installation/dependances
   installation/base-de-donnees

Prérequis
---------

Assurez-vous que votre système dispose des prérequis suivants avant de commencer :

- Python 3.x installé.
- Git installé pour la gestion du code source.
- Un environnement virtuel Python pour isoler les dépendances.

Configuration de l'environnement
-------------------------------

Clonez le référentiel du projet à l'aide de Git et créez un environnement virtuel pour isoler les dépendances Python :

.. code-block:: bash

   git clone https://gitlab.com/giannidevadder/lettings.git
   cd lettings
   python3 -m venv venv
   source venv/bin/activate

Installation des dépendances
---------------------------

Installez les dépendances Python à partir du fichier requirements.txt :

.. code-block:: bash

   pip install -r requirements.txt

Configuration de la base de données
------------------------------------

Configurez votre base de données en utilisant les paramètres Django, puis effectuez les migrations :

.. code-block:: bash

   python manage.py migrate

3. Exécution du projet
=======================

.. toctree::
   :maxdepth: 2

   execution/projet
   execution/developpement
   execution/production

Exécution en mode de développement
----------------------------------

Pour exécuter le projet en mode de développement, utilisez la commande suivante :

.. code-block:: bash

   python manage.py runserver

Le site web sera disponible à l'adresse http://127.0.0.1:8000/.

Exécution en mode de production
-------------------------------

Pour exécuter le projet en mode de production, consultez la section "Déploiement sur Heroku" ci-dessous.

4. Déploiement
==============

.. toctree::
   :maxdepth: 2

   deploiement
   deploiement/heroku
   deploiement/environnement-heroku

Déploiement sur Heroku
-----------------------

Vous pouvez déployer ce projet sur la plateforme Heroku en suivant les étapes suivantes :

1. Créez une application Heroku.
2. Configurez les variables d'environnement nécessaires, y compris SECRET_KEY, DEBUG, SENTRY_DSN et d'autres variables spécifiques à votre projet.
3. Utilisez Heroku Container Registry et Heroku CLI pour déployer l'application. Créez un fichier heroku.yml pour spécifier la commande de démarrage du projet (par exemple, CMD gunicorn lettings.wsgi:application --bind 0.0.0.0:$PORT).
4. Utilisez les outils de gestion des bases de données d'Heroku pour configurer votre base de données.

Personnalisation de l'environnement Heroku
------------------------------------------

Personnalisez davantage votre environnement Heroku en fonction de vos besoins spécifiques.

5. Documentation
===============

.. toctree::
   :maxdepth: 2

   documentation
   documentation/generation
   documentation/acces

Génération de la documentation
-------------------------------

La documentation de ce projet est générée à l'aide de Sphinx. Pour générer la documentation, suivez les instructions dans le fichier doc/README.md.

Accès à la documentation
-------------------------

La documentation est disponible à l'adresse URL de votre documentation.
lien : https://openclassroom-projet-13.readthedocs.io/fr/latest/

6. Support et contact
======================

Si vous avez des questions ou besoin d'assistance, vous pouvez nous contacter à adresse e-mail de support :
giannidevadder0@gmail.com