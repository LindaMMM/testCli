# Commande remote

Installation

### 1. Télécharger le projet sur votre répertoire local :

```
git clone
cd remotecommand
```

### 2. Mettre en place un environnement virtuel :

- Créer l'environnement virtuel: `python -m venv venv`
- Activer l'environnement virtuel :
  - Windows : `venv\Scripts\activate.bat`
  - Unix/MacOS : `source venv/bin/activate`

### 3. Installer les dépendances du projet

```
pip install -r requirements.txt
```

## Démarrage

- Lancer le script à l'aide de la commande suivante : `python -m remotecommand --host 123.0.0.1 --port 12345 `
