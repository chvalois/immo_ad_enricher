input_ad1 = """
VENTE LOUEE Quartier Belleville - Idéalement situé proche des commerces et restaurants de ce quartier vivant, à 5 min à pied de la ligne 11, venez découvrir ce charmant appartement en T1 bis, de 22m2 situé au 2ème étage de cette copropriété bien entretenue. 
A l'intérieur vous découvrirez un espace optimisé grâce à son entrée avec rangements, son séjour lumineux exposé sud-ouest, et sa cuisine ouverte aménagée. 
Un espace en alcôve sert à créer un coin nuit indépendant. Une salle d'eau et des wc séparés complètent ce charmant studio idéal pour un investisseur. Ce bien est vendu loué en bail vide, jusqu'en juin 2026. 
Le montant du loyer est de 806 euros CC. A ne pas rater ! (5.00 pourcent honoraires TTC à la charge de l'acquéreur.)
"""

output_ad1 = """
    Coordonnées du polygone : [[48.8708, 2.3921], [48.8713, 2.3921], [48.8713, 2.3926], [48.8708, 2.3926]]

    Degré de confiance : 95%

    Raisonnement :
    1. Le bien immobilier est situé dans le quartier Belleville, qui est un quartier de la ville de Paris en France.
    2. L'annonce mentionne que le bien est à 5 minutes à pied de la ligne 11. La station de métro la plus proche de Belleville sur la ligne 11 est la station "Belleville", située à l'intersection de la rue de Belleville et de la rue du Faubourg du Temple.
    3. En se basant sur ces informations, le polygone proposé englobe la zone autour de la station de métro "Belleville" et du quartier Belleville à Paris, offrant une couverture probable de la zone où se trouve le bien immobilier mentionné dans l'annonce.
    """

input_ad2 = """
Vente appartement 202 230 €
85 m²
4 pièces
3 chambres
Brumath (67170)
Ajouter aux
FAVORIS

    2 379 €/m² Exclusivité Avec ascenseur 1 terrasse 1 garage - 1 parking Cuisine ouverte, équipée Chauffage individuel au gaz 

SARIMO
SARIMO
30 avis
03 88 35 02 11
Appelez de la part de Superimmo.com
Email
Téléphone
Nom
Bonjour,
Je souhaite avoir plus d’informations sur ce bien. 
Merci de me contacter.
Je souhaite recevoir les annonces similaires. En savoir plus
J’accepte de recevoir les offres de partenaires de Superimmo. En savoir plus

Vos informations sont transmises directement à l'agence afin qu'elle traite votre demande. Voir notre charte des données personnelles.
Vous rencontrez un problème sur le site ?
Merci de nous signaler le problème
Description

EXCLUSIVITÉ SARIMO - SPÉCIAL INVESTISSEUR
Laissez-vous charmer par ce charmant appartement 4 pièces de 85 m², idéal pour un investisseur.
Situé dans une petite copropriété de deux étages à 20 minutes du centre-ville de STRASBOURG et à proximité de toute commodité en plein coeur de la commune de BRUMATH.
Loyer : 750€ + 120€ charges.
Date d'écheance du bail : 05/2026
Le bien est composé de :
- Un séjour lumineux de 22 m².
- Une cuisine US aménagée et équipée (four, plaque de cuisson, hotte, lave-vaisselle...).
- Trois belles chambres.
- Une salle de bain avec baignoire et meuble vasque.
- Un WC séparé.
En extérieur, le bien bénéficie également d'une belle terrasse de 10 m2, offrant ainsi un emplacement extérieur exceptionnel pour profiter des beaux jours.
LA VALEUR AJOUTÉE : Un garage en box au sous-sol - Une place de parking - Une cave.
Chauffage et eau chaude au gaz individuel - Menuiserie double vitrage en PVC.
A propos de la copropriété : Pas de procédure en cours
Nombre de lots principaux : 36
Charges prévisionnelles annuelles : €
Les informations sur les risques auxquels ce bien est exposé sont disponibles sur le site Géorisques : www.georisques.gouv.fr.
Date de réalisation du diagnostic : 22/11/2012
Le prix indiqué comprend les honoraires à la charge de l'acheteur : 7 % TTC du prix du bien hors honoraires.
Prix hors honoraires : 189 000 €
Montant estimé des dépenses annuelles d'énergie pour un usage standard : entre 589 € et 840 € par an.
Prix moyens des énergies indexés sur l'année 2010 (abonnements compris).
Honoraires inclus de 7% à la charge de l'acquéreur. Prix hors honoraires 189 000 €. Dans une copropriété de 36 lots. Aucune procédure n'est en cours. Classe énergie C, Classe climat D. Montant moyen estimé des dépenses annuelles d'énergie pour un usage standard, établi à partir des prix de l'énergie de l'année 2010 : 818.00 €. Date de réalisation du DPE : 22-11-2012. Les informations sur les risques auxquels ce bien est exposé sont disponibles sur le site Géorisques : georisques.gouv.fr.
"""

output_ad2 = """
    Coordonnées du polygone : [[48.715, 7.716], [48.715, 7.725], [48.708, 7.725], [48.708, 7.716]]

    Degré de confiance : 95%
    Raisonnement :
    1. L'annonce mentionne que le bien est situé à Brumath (67170).
    2. Il est précisé que l'appartement est à 20 minutes du centre-ville de Strasbourg, ce qui confirme la localisation à proximité de Strasbourg.
    3. La description met en avant la commune de Brumath et ses commodités, confirmant davantage la localisation dans cette zone.
    4. Les coordonnées du polygone sont déterminées autour de Brumath, en prenant en compte sa position géographique par rapport à Strasbourg et les informations fournies dans l'annonce.
    """

input_wrong1 = "What did the cow say to the moon?"
output_wrong1 = "Ceci ne semble pas correspondre à une annonce immobilière"

input_wrong2 = "Write me a poem about the moon"
output_wrong2 = "Ceci ne semble pas correspondre à une annonce immobilière"