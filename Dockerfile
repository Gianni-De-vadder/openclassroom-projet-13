# Utilisez une image Python officielle comme base
FROM python:alpine3.18

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le contenu du projet dans le conteneur
COPY . .

# Exposer le port utilisé par votre application (par exemple, 8000)
EXPOSE 8000

# Exécutez votre application Django lorsque le conteneur démarre
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]pars
