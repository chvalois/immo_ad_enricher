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

output_immoreview_ad1 = """
Voici l'évaluation de l'annonce pour le bien immobilier décrit :

Taille du bien : 5/10
Avec une superficie de 22 m², l'appartement est relativement petit, ce qui peut convenir à un investisseur ou à une personne seule, mais limite son attrait pour une famille.

Luminosité du bien : 8/10
Le séjour est décrit comme "lumineux exposé sud-ouest", ce qui est un atout majeur pour la luminosité de l'appartement. Cela suggère une bonne exposition à la lumière naturelle.

Proche des commerces : 9/10
L'annonce mentionne que l'appartement est situé "proche des commerces et restaurants" dans un quartier vivant, ce qui indique une excellente accessibilité aux commodités.

Proche de la nature : 6/10
L'annonce ne mentionne pas directement la proximité de parcs ou d'espaces verts, mais le jardin sans vis-à-vis peut offrir un petit espace naturel. Cependant, l'absence de détails sur des espaces naturels à proximité limite la note.

Environs calmes et sans nuisance sonore : 7/10
Bien que le quartier soit vivant, l'appartement est décrit comme ayant un "joli jardin orienté sud, sans vis-à-vis", ce qui suggère un certain niveau de tranquillité, mais la proximité des commerces peut engendrer des nuisances sonores.

Modernité du bien : 8/10
L'appartement est décrit comme ayant un espace optimisé avec une cuisine ouverte aménagée et un agencement fonctionnel, ce qui indique une certaine modernité. Toutefois, des détails supplémentaires sur les équipements modernes auraient pu renforcer cette note.

Bonus du bien : 7/10
Bien que l'appartement ne dispose pas de bonus tels qu'une piscine ou une terrasse, le jardin sans vis-à-vis est un atout appréciable. De plus, l'agencement optimisé et l'espace en alcôve pour un coin nuit ajoutent de la valeur.
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

output_immoreview_ad2 = """
Voici l'évaluation de l'annonce pour le bien immobilier décrit :

Taille du bien : 8/10
Avec 85 m² pour un appartement de 4 pièces, la taille est raisonnable et adaptée pour une famille ou un investisseur. Cela mérite une bonne note.

Luminosité du bien : 7/10
Le séjour est décrit comme "lumineux", ce qui est un bon indicateur de luminosité. Toutefois, le manque d'informations sur l'orientation des fenêtres ou d'autres éléments pouvant influencer la luminosité empêche d'atteindre une note maximale.

Proche des commerces : 8/10
L'annonce mentionne que l'appartement est situé "à proximité de toute commodité", ce qui indique une bonne accessibilité aux commerces. Cela mérite une note élevée, bien que des détails supplémentaires sur la distance ou le type de commerces auraient pu justifier une note parfaite.

Proche de la nature : 5/10
L'annonce ne fait pas mention de la proximité de parcs ou d'espaces naturels. En l'absence d'informations sur ce point, la note est neutre.

Environs calmes et sans nuisance sonore : 6/10
Bien que l'appartement soit situé dans une petite copropriété et à 20 minutes du centre-ville de Strasbourg, il n'y a pas d'indication explicite sur le niveau de bruit ambiant. Cela laisse supposer un environnement relativement calme, mais pas garanti.

Modernité du bien : 7/10
L'appartement dispose d'équipements modernes comme une cuisine ouverte aménagée et équipée, ainsi que des menuiseries en double vitrage. Cependant, l'âge de la construction n'est pas précisé, ce qui empêche d'atteindre une note plus élevée.

Bonus du bien (comme piscine, terrasse, dépendance) : 9/10
L'appartement bénéficie d'une belle terrasse de 10 m², d'un garage en box, d'une place de parking et d'une cave. Ces éléments ajoutent une valeur significative au bien, justifiant une note élevée."""


input_ad3 = """
MEUDON - VAL FLEURY : L'agence STONEO vous propose en exclusivité un appartement de 3 pièces de 54 m², situé dans une rue calme au rez-de-chaussée surélevé d’un immeuble de 1930 récemment ravalé. Les professions libérales sont autorisées dans l’immeuble.
Il bénéficie d’un agencement efficace en étoile et traversant. Il se compose d’une entrée desservant deux premières pièces pouvant être réunies afin de créer un espace de vie de plus 22 m², d’une grande chambre de 13m² donnant sur cour, ainsi qu’une cuisine séparée, une salle d’eau et des WC séparés.
Ce bien à rénover conserve encore tout le charme de l’ancien notamment avec sa belle hauteur sous plafond (3,2m), son parquet, ses carreaux de ciment ou encore ses grandes fenêtres.
Plusieurs options de réagencement sont possibles à l’occasion de la rénovation de cet appartement, parmi lesquelles la possibilité de créer une chambre bébé ou un bureau et d’aménager une cuisine moderne dans le séjour.
Il est possible d’exercer une profession libérale avec 3 cabinets et une salle d’attente.
La copropriété est située au pied des commerces (boulangerie, Monoprix, pharmacie, restaurants…) et à proximité immédiate de la gare de Val Fleury (RER C reliant Paris Champ de Mars en 15 min).
Avec plus de 200 ventes cette année, STONEO s’est affirmée comme une agence immobilière incontournable à Paris. Notre équipe dynamique et expérimentée, notre maîtrise des dernières innovations digitales, notre fichier de plus de 5 000 acheteurs actifs et la mise en place de stratégies de commercialisation personnalisées vous garantissent un accompagnement sans égal pour vos projets d’achat et de vente. Nos clients sont satisfaits (4.9/5 sur Google) et nous recommandent. Notre agent Laurent FEDIDA se tient à votre disposition pour tout complément d'informations.
"""

output_ad3 = """
Coordonnées du polygone : [[48.811, 2.236], [48.811, 2.245], [48.804, 2.245], [48.804, 2.236]]

Degré de confiance : 90%

Raisonnement :
1. L'annonce mentionne spécifiquement que l'appartement est situé à Meudon, dans le quartier de Val Fleury, ce qui limite l'emplacement.
2. Les coordonnées GPS fournies pour la Gare de Val Fleury (48.8079618, 2.2409902606521745) confortent l'emplacement, étant donné la proximité immédiate avec la gare et les commerces.
3. En tenant compte de la description qui indique que le bien est proche des commerces et à une distance courte de la gare, j'ai tracé un polygone autour de la gare incluant les zones commerçantes et résidentielles voisines.
4. Les points de coordonnées créent un espace suffisamment grand autour de la gare, en respectant la zone mentionnée dans l'annonce, ce qui garantit que le bien immobilier proposé se situe bien à l'intérieur du polygone dans le quartier de Val Fleury à Meudon.
"""

input_places_ad1 = """
BORDEAUX JARDIN PUBLIC

Située à proximité immédiate du Jardin Public, cette belle maison en pierre est agrémentée d'une terrasse en rooftop de 25 m². Elle vous propose au rez-de-chaussée une belle pièce de réception avec des murs en pierres apparentes. La cuisine ouverte est équipée et dispose d'un cellier. Son escalier en pierre mène au premier étage. Le palier dessert trois chambres avec parquets et une salle d'eau. Au deuxième et dernier étage un salon d'été s'ouvre sur une agréable terrasse tropézienne sans vis-à-vis ! Un bien de qualité dans un secteur calme et résidentiel en plein centre ville à venir découvrir.
Contactez-nous au 05 56 00 25 00 ou au 05 56 45 51 01
"""

output_places_ad1 = """
[Jardin Public (Bordeaux)]
"""

input_places_ad2 = """
Paris, Idéalement situé entre le Square Louvois et le Jardin du Palais Royal, cet appartement traversant de 103,21 (102,21 m2 Carrez), 
u charme incontestable, prend place au cinquième étage (avant-dernier étage) d'un immeuble datant du 17ème siècle (ascenseur à l'étude). 

L'ensemble, nécessitant une rénovation complète, se compose de trois pièces principales : deux donnant sur la rue et deux autres donnant sur une cour intérieure, 
offrant une modularité intéressante des espaces et la possibilité d'une rénovation sur mesure. Une cuisine ainsi qu'une salle de bains complètent cet espace. 

Le charme de l'ancien, caractérisé par les poutres apparentes et les deux magnifiques cheminées d'époque, associé au potentiel de rénovation, 
font de cet appartement un bien rare au sein d'un quartier hyper prisé. Une cave vient compléter ce bien soumis au statut de la copropriété. 

Métro Pyramides, Palais Royal et Quatre septembre (lignes 1, 3, 7 et 14)
"""

output_places_ad2 = """
[Square Louvois (Paris), Jardin du Palais Royal (Paris)]
"""


input_wrong1 = "Quels sont les documents utilisés dans cette application ?"
output_wrong1 = "Ceci ne semble pas correspondre à une annonce immobilière"

input_wrong2 = "Ecris moi une annonce immobilière pour une maison à Bordeaux"
output_wrong2 = "Je suis une application qui analyse les annonces immobilières, mais je ne suis pas habilité à rédiger une annonce à la demande."

input_wrong3 = """
Description
En tant que passionné de PC gamer, j'ai décidé de lancer mon entreprise pour proposer, selon mon point de vue, les meilleurs PC gamer possibles. Je suis ici avant tout pour t'aider à faire le bon choix !

Mon entreprise MFP Computer te présente le PC GAMER “Nexus”, construit à partir de composant complétement neuf !

🟦Processeur: Ryzen 7 5700X (neuf)

🟦Ventirad: Thermalright AssassinX120 SE ARGB (neuf)

🟦Carte mère: MSI B550 PRO-VDH (neuf)

🟦RAM: Team Group 16 GB (2x8) DDR4-3200 (neuf)

🟦Carte graphique: RTX 4070 SUPER 12GB MSI VENTUS (neuf)

🟦SSD: 1To Kingston NV2 NVMe M.2 (neuf)

🟦Alimentation: Seasonic B12 BC-750 750W 80 Plus Bronze (neuf)

🟦Boîtier: MSI 112R (neuf)

-Windows 11 PRO installé + activé✅
-Pc déjà monté, prêt à l'emploi

🎮Performances du pc disponible en photos !🎮

Rendez-vous sur notre site internet (mfpcomputer.com) pour plus de photos, détails et d'options !

✅ 2 ans de garantie sur tous les composants ✅

▶️Prix : 1279€ ✅ (FERME et PAS D'ÉCHANGES)
▶️Envoi possible ✅
☎️N'hésitez pas à nous contacter, on vous répondra avec plaisir ! 😊
"""
output_wrong3 = "Ceci ne semble pas correspondre à une annonce immobilière"
