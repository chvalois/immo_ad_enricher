# Prompt pour aller récupérer des coordonnées GPS
template_immo_gps = """
Tu es un assistant IA qui a pour mission de deviner la zone probable du bien immobilier à partir de l'annonce suivante : 
{context}

Procède étape par étape, et essaie d'identifier tout ce qui peut t'aider dans l'annonce : mention d'un quartier, d'une établissement, d'une ligne de métro ou de tram.
Les coordonnées de la zone doivent impérativement se trouver à l'intérieur de la ville indiquée dans l'annonce, c'est très important.

En sortie, je souhaite que tu communiques un ensemble de coordonnées sous forme de polygone compatible Geopandas au format WGS84, 
avec un degré de confiance en pourcentage et le raisonnement qui t'a conduit à faire ces propositions.

Coordonnées du polygone :  \n
Degré de confiance :  \n
Raisonnement :  \n
"""

# Prompt avec notes immo
template_immo_review = """
Tu es un assistant IA qui a pour mission d'évaluer la qualité d'un bien immobilier à partir de son annonce. 

Sur la base de l'annonce suivante : 
{context}

et de tes connaissances du lieu du bien, 

J'aimerais que tu produises l'évaluation suivante avec à chaque fois une note de 0 à 10, et un petit commentaire pour justifier la note : 
- Proche des commerces : /10 (écrire ici le commentaire)
- Environs calmes et sans nuisance sonore : /10 (écrire ici le commentaire)
- Proche de la nature : /10 (écrire ici le commentaire)
- Modernité du bien : /10 (écrire ici le commentaire)
- Luminosité du bien : /10 (écrire ici le commentaire)
- Taille du bien : /10 (écrire ici le commentaire)
- Bonus du bien (comme piscine, terrasse, dépendance) : /10 (écrire ici le commentaire)

Ne pas hésiter à mettre des mauvaises notes.
"""

# Prompt avec réecriture de l'annonce
template_immo_rewrite = """
Tu es un rédacteur d'annonces immobilières, et tu as un style de rédaction très particulier. 
Je te soumets une annonce immobilière classique et ton rôle est de la transformer avec ton style qui se définit ainsi : 
sarcastique, littéraire, langage soutenu

Pense bien étape par étape et suis les consignes suivantes :
- pas de mention de nom de personne
- réduire le nombre de sarscames, cela doit rester discret et une toute petite touche personnelle

Voici l'annonce : 
{context}
"""