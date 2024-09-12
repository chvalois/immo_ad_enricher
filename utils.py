import re
import plotly.express as px
import pandas as pd
import requests
import time

def extract_polygon(text):
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

def generate_polygon_on_map(text):

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

def extract_reviews(text):
    # Define a dictionary to store the extracted ratings
    reviews = {}

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

def display_radar(reviews):
    df = pd.DataFrame(list(reviews.items()), columns=['critere', 'note'])
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


def get_gps_coordinate(place): 

    # Define the base URL for the API
    url = "https://nominatim.openstreetmap.org/search"

    # Get a copy of the default headers that requests would use
    headers = requests.utils.default_headers()

    headers.update(
        {
        'User-Agent': 'My User Agent 1.0',
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

    if response.status_code != 204:

        # Parse the response as JSON
        data = response.json()

        lat = data[0]['lat']
        lon = data[0]['lon']

    return lat, lon

def get_ad_with_gps(ad, answer_places):
    places_gps = "\n Coordonnées des lieux mentionnés dans l'annonce : \n"

    list_of_places = extract_list(answer_places)
    print(list_of_places)

    if ((list_of_places != []) & (list_of_places != [''])):

        for place in list_of_places:
            lat, lon = get_gps_coordinate(place)
            places_gps = places_gps + (f"{place}: {lat}, {lon} \n")
            time.sleep(1)

        ad_desc_improved = ad + places_gps
    else:
        places_gps = ""
        ad_desc_improved = ad
    
    return places_gps, ad_desc_improved

def calculate_time(start, end):
    time = f"{round(end-start, 2)}s"
    return time