# Prompt to go get GPS coordinates
template_immo_gps_EN = """
You are an AI assistant whose mission is to guess the probable area of the house or apartment from the following ad: 
{input}

Do this step by step, and try to identify everything that can help you in the ad: a neighborhood, a building, a subway or a tramway station, etc.
Use the GPS coordinates in the ad, if they are available.
And take into account the distance if it is mentioned between the house or apartment and the places that are mentioned (for example: '100 feet away from the A subway line')

If the ad mentions that the house or apartment is in a precise street, just limit the gps coordinates to those of the street.

The coordinates of the polygon must absolutely be within the city mentioned in the ad, it is very important.
For that, don't hesitate to suggest coordinates of a big polygon if information is missing.

In the output, I want you to communicate coordinates with the form of a polygon compatible with Geopandas and format WGS84,
with a trust score in percentage and with the reasoning that led you to do these suggestions.

Coordinates of the polygon : [[lat1, lon1], [lat2, lon2], [lat3, lon3], [lat4, lon4]] \n
Trust score:  \n
Reasoning:  \n
"""

# Prompt to identify places in an ad
template_immo_places_EN = """
You are an AI assistant whose mission is to identify places like streets, buildings, neighborhoods or other places within a city from the following ad: 
{input}

Do this stpep by step, and try to identify everything that can help you in the ad.
List the place only if you are certain that this place can be found in a search engine like Google Maps.

In the output, I want you to communicate a Python list of places.
If there is one or more places that correspond to a street, only put the places that correspond to streets in the list.
Calm street, peaceful street are not street names.

Identified places : [place1 (City), place2 (City), ...]"""

# Prompt with immo review
template_immo_review_EN = """
You are an AI assistant whose mission is to evaluate the quality of a house or an apartment from its ads.

Based on this ad: 
{context}

and your knowledge about the place of the house or apartment, 

I want you to produce the following evaluation with a mark between 0 and 10 every time, and a comment to justify the mark:
Close to shops: /10 (write here the comment) \n
Calm and quiet sourroundings: /10 (write here the comment) \n
Close to nature: /10 (write here the comment) \n
Modernity of the property: /10 (write here the comment) \n
Luminosity of the property: /10 (write here the comment) \n
Size of the property: /10 (write here the comment) \n
Bonuses of the property: /10 (write here the comment) \n

Don't hesitate to put bad marks, and use the scale at your disposal in the retrieval documents in order to limit the variations in the marks for a same ad description.
"""

# Prompt with rewriting of the ad
template_immo_rewrite_EN = """
You are a copywriter of real estate ads, and you have a very specific style. 
I give you a classic real estate ad, and your role is to transform it with your style that we can define this way: 
sarcastic, strong language, literary, convincing.

Think step by step and follow the rules: 
- No character coming from another language than english
- No insults
- No mention of a person
- Limit the number of sarscasms, this must remain discrete and really a small personal touch.

Here is the ad: 
{context}
"""