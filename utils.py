import re
import plotly.express as px
import pandas as pd

def extract_polygon(text):
    # Regex pattern to match [[]]
    polygon_pattern = r'\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]'
    
    # Find all matches in the text
    matches = re.findall(polygon_pattern, text)
    matches.append(matches[0])

    # Convert matches to float and back to list format
    polygon = [[float(lat), float(lon)] for lat, lon in matches]
    return polygon

def generate_polygon_on_map(text):

    polygon = extract_polygon(text)
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

    # Print the results
    for key, value in reviews.items():
        print(f"{key} = {value}")

    return reviews

def display_radar(reviews):
    df = pd.DataFrame(list(reviews.items()), columns=['critere', 'note'])

    print(df.head())
    fig = px.line_polar(df, r='note', theta='critere', line_close=True)
    fig.update_traces(fill='toself')
    return fig


# Function to display stars based on a rating (out of 10)
def display_stars(rating, max_rating=10):
    stars = "⭐" * int(rating / max_rating * 5)  # Convert 0-10 scale to 0-5 stars
    
    # st.write("Rating: ", rating)
    # st.write(display_stars(rating))