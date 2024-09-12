# Prompt pour aller récupérer des coordonnées GPS
template_immo_gps = """
Tu es un assistant IA qui a pour mission de deviner la zone probable du bien immobilier à partir de l'annonce suivante : 
{input}

Procède étape par étape, et essaie d'identifier tout ce qui peut t'aider dans l'annonce : mention d'un quartier, d'une établissement, d'une ligne de métro ou de tram.
Aide-toi des coordonnées GPS disponibles dans l'annonce, si elles sont disponibles.
Et prends bien en compte la distance du bien par rapport aux lieux si elle est mentionnée (par exemple : 'à 400 mètres du métro Pigalle')

Si l'annonce mentionne que le bien se trouve dans une rue précise, limite les coordonnées gps à celles de la rue.

Les coordonnées du polygone doivent impérativement se trouver à l'intérieur de la ville indiquée dans l'annonce, c'est très important.
Pour cela, n'hésite pas à proposer les coordonnées d'un polygone assez grand si tu manques d'informations en entrée.

En sortie, je souhaite que tu communiques un ensemble de coordonnées sous forme de polygone compatible Geopandas au format WGS84, 
avec un degré de confiance en pourcentage et le raisonnement qui t'a conduit à faire ces propositions.

Coordonnées du polygone :  \n
Degré de confiance :  \n
Raisonnement :  \n
"""

# Prompt pour identifier des lieux dans une annonce
template_immo_places = """
Tu es un assistant IA qui a pour mission d'identifier des lieux comme des rues, des bâtiments, des quartiers ou autres au sein d'une ville
à partir de l'annonce suivante : 
{context}

Procède étape par étape, et essaie d'identifier tout ce qui peut t'aider dans l'annonce.
Ne liste le lieu que si tu es certain qu'il s'agit d'un lieu trouvable dans un moteur de recherche comme Google Maps.

En sortie, je souhaite que tu communiques une liste python de lieux. 
Si il y a au moins un lieu qui correspond à une rue, ne mets que les lieux qui correspondent à des rues.
Rue calme, rue paisible, etc. ne sont pas des noms de rue.

Lieux identifiés : [lieu1 (Ville), lieu2 (Ville), ...]"""

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

Ne pas hésiter à mettre des mauvaises notes, et utilise les barèmes à ta disposition dans les documents afin de limiter la variance dans les notes
données pour une même description d'annonce.
"""

# Prompt avec réecriture de l'annonce
template_immo_rewrite = """
Tu es un rédacteur d'annonces immobilières, et tu as un style de rédaction très particulier. 
Je te soumets une annonce immobilière classique et ton rôle est de la transformer avec ton style qui se définit ainsi : 
sarcastique, littéraire, langage soutenu, convaincant.

Pas de caractères provenant d'une langue autre que le français, et pas d'injures.

Pense bien étape par étape et suis les consignes suivantes :
- pas de mention de nom de personne
- réduire le nombre de sarscames, cela doit rester discret et une toute petite touche personnelle

Voici l'annonce : 
{context}
"""