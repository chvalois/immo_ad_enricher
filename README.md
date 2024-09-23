# Immo Ad Analyzer
==================

Cette application permet d'analyser la description des annonces de biens immobiliers à l'aide de LLM.

Stack : 
- Langchain
- Langsmith
- API Open AI
- Streamlit

L'application est disponible en français et en anglais :
![image](https://github.com/user-attachments/assets/b47f6027-3f80-4e4e-9ec7-f658891129d0)

A partir d'une annonce, l'application renvoie 3 rubriques : 

**1. Review du bien immobilier**

A l'aide d'un RAG, le modèle LLM a été entraîné à donner des notes selon un barème aux différentes caractéristiques des biens, tels qu'ils sont décrits dans l'annonce : 

![Review d'une annonce immobilière](resources/immo_review.png)

**2. Coordonnées probables du bien**

Une première requête à l'API Open AI permet d'identifier les lieux mentionnés dans l'annonce.
Ces lieux font l'objet d'une requête à l'API Nominatim qui permet d'associer des coordonnées GPS aux lieux identifiés.
Une seconde requête renvoie un polygone de coordonnées GPS, correspondant à la zone probable du bien : 

![Coordonnées probables du bien immobilier](resources/immo_gps.png)

**3. Réécriture de la description du bien dans un style plus ... personnel**

Un simple test de l'API Open AI.
A partir d'un prompt personnalisé, l'API renvoie une description dans un style littéraire et légèrement sarcastique : 

![Réécriture de l'annonce](resources/immo_rewrite.png)

# Utilisation de l'application
==============================

Création de votre environnement en local
`python -m venv .venv`

Activation de l'environnement sous windows
`.venv\scripts\activate`

Installation des packages
`pip install -r requirements.txt`

Dupliquer le contenu du fichier .env.example dans un fichier .env que vous devez créer à la racine du projet
Et insérer vos clés API : 
OPENAI_API_KEY (obligatoire)
LANGCHAIN_API_KEY (non obligatoire)

Lancement de l'application
`streamlit run app.py`

Pour utiliser votre propre RAG pour la génération des reviews, indiquer le répertoire contenant les fichiers PDF :
`python -m context_docs --filepath "./path/to/your_pdf_files_directory" --collection_name "immo_review”`

