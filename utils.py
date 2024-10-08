import re
import plotly.express as px
import pandas as pd
import requests
import time
import os
import streamlit as st
from browser_detection import browser_detection_engine

def extract_polygon(text):
    """
    Retourne une liste de [Latitude, Longitude] permettant de générer un polygone via Regex

    Paramètres
    -------
    text : str | texte brut issu du LLM
    
    Retourne
    -------
    polygon : list
    """ 

    # Regex pattern to match [[]]
    polygon_pattern = r'\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]'
    
    # Find all matches in the text
    try:
        matches = re.findall(polygon_pattern, text)
        matches.append(matches[0])

        # Convert matches to float and back to list format
        polygon = [[float(lat), float(lon)] for lat, lon in matches]
    except:
        print(f"Polygon was not found in {text}")
        polygon = []
    
    return polygon


def extract_list(text):
    """
    Retourne une liste au sein d'un texte via Regex

    Paramètres
    -------
    text : str | texte brut issu du LLM
    
    Retourne
    -------
    extracted_list : list
    """ 
        
    # Regex pattern to match [[]]
    list_pattern = r'\[(.*?)\]'
    
    # Use re.search to find the list within square brackets
    match = re.search(list_pattern, text)

    # Check if there was a match
    if match:
        # Extract the captured list (removing any quotes)
        extracted_list = match.group(1)
        
        # Split the result by commas to get individual items
        extracted_list = [item.strip().strip('"') for item in extracted_list.split(',')]
    else:
        extracted_list = []
        print("No list found")
    
    return extracted_list

def extract_reviews(text, language):
    """
    Retourne les notes attribués à chaque élément de l'annonce via Regex

    Paramètres
    -------
    text : str | texte brut issu du LLM
    
    Retourne
    -------
    reviews : dict
    """ 

    # Define a dictionary to store the extracted ratings
    reviews = {}

    if language == 'EN':
        # Define regex to match the rating patterns
        pattern_proche_comm = r"Close to shops: (\d+)/10"
        pattern_calme = r"Calm and quiet surroundings: (\d+)/10"
        pattern_proche_nature = r"Close to nature: (\d+)/10"
        pattern_moderne = r"Modernity of the property: (\d+)/10"
        pattern_luminosite = r"Luminosity of the property: (\d+)/10"
        pattern_taille = r"Size of the property: (\d+)/10"
        pattern_bonus = r"Bonuses of the property: (\d+)/10"
    
    else:
        # Define regex to match the rating patterns
        pattern_proche_comm = r"Proche des commerces : (\d+)/10"
        pattern_calme = r"Environs calmes et sans nuisance sonore : (\d+)/10"
        pattern_proche_nature = r"Proche de la nature : (\d+)/10"
        pattern_moderne = r"Modernité du bien : (\d+)/10"
        pattern_luminosite = r"Luminosité du bien : (\d+)/10"
        pattern_taille = r"Taille du bien : (\d+)/10"
        pattern_bonus = r"Bonus du bien \(comme piscine, terrasse, dépendance\) : (\d+)/10"
        
    try:
        matches = re.findall(pattern_proche_comm, text)
        reviews['review_proche_comm'] = int(matches[0])
    except:
        pass

    try:
        matches = re.findall(pattern_calme, text)
        reviews['review_calme'] = int(matches[0])
    except:
        pass

    try:
        matches = re.findall(pattern_proche_nature, text)
        reviews['review_proche_nature'] = int(matches[0])
    except:
        pass

    try:
        matches = re.findall(pattern_moderne, text)
        reviews['review_moderne'] = int(matches[0])
    except:
        pass

    try:
        matches = re.findall(pattern_luminosite, text)
        reviews['review_luminosite'] = int(matches[0])
    except:
        pass

    try:
        matches = re.findall(pattern_taille, text)
        reviews['review_taille'] = int(matches[0])
    except:
        pass

    try:
        matches = re.findall(pattern_bonus, text)
        reviews['review_bonus'] = int(matches[0])
    except:
        pass

    return reviews

def generate_polygon_on_map(text):
    """
    Génère un polygone sur une cartographie Mapbox via Plotly

    Paramètres
    -------
    text : str | texte brut issu du LLM
    
    Retourne
    -------
    fig : figure ploty express
    """ 

    polygon = extract_polygon(text)
    print(polygon)
    lat, lon = zip(*polygon)

    # Create Plotly map with Mapbox
    fig = px.scatter_mapbox(
        lat=lat,
        lon=lon,
        mapbox_style="open-street-map",  # You can change this to 'satellite', 'outdoors', etc.
        zoom=13
    )
    fig.update_traces(mode='lines+markers')
    return fig

def display_radar(reviews, language):
    """
    Génère un graphique de type Radar Plot via Plotly à partir des reviews

    Paramètres
    -------
    reviews : dict
    
    Retourne
    -------
    fig : figure ploty express
    """ 

    df = pd.DataFrame(list(reviews.items()), columns=['critere', 'note'])

    if language == 'EN':
        replace_dict = {'review_calme': 'Calm surroundings',
                        'review_proche_nature': 'Close to nature',
                        'review_moderne': 'Modernity',
                        'review_luminosite': 'Luminosity',
                        'review_taille': 'Size of the property',
                        'review_bonus': 'Bonuses of the property',
                        'review_proche_comm': 'Close to shops'}
    else:
        replace_dict = {'review_calme': 'Calme',
                        'review_proche_nature': 'Proche de la nature',
                        'review_moderne': 'Modernité du bien',
                        'review_luminosite': 'Luminosité du bien',
                        'review_taille': 'Taille du bien',
                        'review_bonus': 'Bonus du bien',
                        'review_proche_comm': 'Proche des commerces'}

    df['critere'] = df['critere'].replace(replace_dict)

    fig = px.line_polar(df, r='note', theta='critere', line_close=True)
    fig.update_traces(fill='toself')

    # Set maximum radial axis value to 10
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                range=[0, 10],  # Set range from 0 to 10
                tickvals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Custom tick values
            )
        )
    )

    return fig

def get_user_agent():
    try:
        browser = browser_detection_engine(singleRun=True)
        user_agent = browser['userAgent']
    except:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"    

    return user_agent

def get_gps_coordinate(place, user_agent): 
    """
    Retourne les coordonnées GPS les plus probables d'un lieu via API Nominatim

    Paramètres
    -------
    place : str | nom d'une rue et de la ville ou quartier ou bâtiment
    
    Retourne
    -------
    lat : float
    lon : float
    """ 

    lat, lon = (0.0000, 0.0000)

    # Define the base URL for the API
    url = "https://nominatim.openstreetmap.org/search"

    # Get a copy of the default headers that requests would use
    headers = requests.utils.default_headers()

    headers.update(
        {
        'User-Agent': user_agent,
        }
    )

    # Define the parameters for the query
    params = {
        'q': place,  # Replace this with the address or location
        'format': 'json',  # Specify the response format as JSON
        'limit': 1,  # Return only one result
        'addressdetails': 1  # Include detailed address information in the result
    }

    # Send the GET request to the API
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:

        # Parse the response as JSON
        data = response.json()

        lat = data[0]['lat']
        lon = data[0]['lon']

    return lat, lon

def get_ad_with_gps(ad, answer_places, user_agent, language):
    """
    Retourne l'annonce origine enrichie des lieux identifiés dans l'annonce et de leurs coordonnées GPS

    Paramètres
    -------
    ad : str | annonce origine
    answer_places : str | réponse du LLM sur les lieux identifiés dans l'annonce
    user_agent : str
    
    Retourne
    -------
    places_gps : str | lieux identifiés avec leurs coordonnées gps
    ad_desc_improved : str | annonce enrichie de la liste des lieux identifiés
    """ 
        
    if language == 'EN':
        places_gps = "\n Coordinates of places mentioned in the ad: \n"
    else:
        places_gps = "\n Coordonnées des lieux mentionnés dans l'annonce : \n"

    list_of_places = extract_list(answer_places)
    print(list_of_places)

    if ((list_of_places != []) & (list_of_places != [''])):

        for place in list_of_places:
            lat, lon = get_gps_coordinate(place, user_agent)

            if (lat != 0.0000) and (lon != 0.0000):
                places_gps = places_gps + (f"{place}: {lat}, {lon} \n")
            time.sleep(1)

        ad_desc_improved = ad + places_gps
    else:
        places_gps = ""
        ad_desc_improved = ad
    
    return places_gps, ad_desc_improved

def calculate_time(start, end):
    """
    Retourne le temps écoulé entre start et end

    Paramètres
    -------
    start : float
    end : float
    
    Retourne
    -------
    time : float
    """ 
        
    time = f"{round(end-start, 2)}s"
    return time