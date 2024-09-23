import streamlit as st
import logging
import time
import platform

from llm import get_immo_xy_gpt4_fewshots, get_immo_review, get_immo_rewrite, get_immo_places
from prompts import template_immo_gps, template_immo_review, template_immo_rewrite, template_immo_places
from prompts_EN import template_immo_gps_EN, template_immo_review_EN, template_immo_rewrite_EN, template_immo_places_EN
from utils import generate_polygon_on_map, extract_reviews, display_radar, get_ad_with_gps, calculate_time, get_user_agent

if platform.system() == "Linux":
    # Import packages for Linux
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

st.cache_data.clear()
st.cache_resource.clear()
st.set_page_config(layout="wide")

user_agent = get_user_agent()


#### ---- Logging ---- ####

logging.basicConfig(filename='app.log',   # Log file name
                    filemode='w',         # 'w' to overwrite, 'a' to append
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
                    level=logging.INFO)   # Set the log level


st.title("Immo Ad Analyzer")

# Description de l'annonce
language = st.selectbox('', ['FR', 'EN'])

if language == 'EN':
    ad_desc = st.text_area("Copy / Paste here the description of the ad. The description must contain the name of the city.", height=250)
    please_desc_message = "Please enter a valid description"
    button_message = "Start Analysis"
else:
    ad_desc = st.text_area("Copier / Coller ici la description de l'annonce. La description doit impérativement inclure le nom de la ville.", height=250)
    please_desc_message = "Veuillez renseigner une description"
    button_message = "Lancer l'analyse"


if st.button(button_message):

    if ad_desc:
        start = time.time()

        if language == 'EN':
            template_immo_review = template_immo_review_EN
            template_immo_places = template_immo_places_EN
            template_immo_gps = template_immo_gps_EN
            template_immo_rewrite = template_immo_rewrite_EN
            waiting_message = "Please wait ..."
            review_message = "Review of the property"
            gps_message = "Probable location of the property"
            rewrite_message = "Rewriting of the ad"
        else:
            waiting_message = "Veuillez patienter ..."
            review_message = "Review du bien immobilier"
            gps_message = "Coordonnées probables du bien immobilier"
            rewrite_message = "Réécriture de l'annonce"            

        with st.spinner(waiting_message):
            logging.info("")
            answer_review = get_immo_review(ad_desc, template_immo_review, language)
            st.subheader(review_message)

            reviews = extract_reviews(answer_review, language)
            fig = display_radar(reviews, language)
            st.plotly_chart(fig)
            st.write(answer_review)

            immo_review_time = time.time()
            logging.info(f"Immo Review - {calculate_time(start, immo_review_time)}")

        with st.spinner(waiting_message):
            answer_places = get_immo_places(ad_desc, template_immo_places, language)
            places_gps, ad_desc_improved = get_ad_with_gps(ad_desc, answer_places, user_agent, language)

            answer_gps = get_immo_xy_gpt4_fewshots(ad_desc_improved, template_immo_gps, language)

            st.subheader(gps_message)
            st.write(places_gps)
            fig = generate_polygon_on_map(answer_gps)
            st.plotly_chart(fig)
            st.write(answer_gps)

            immo_places_time = time.time()
            logging.info(f"Immo Guess GPS - {calculate_time(immo_review_time, immo_places_time)}")

        with st.spinner(waiting_message):
            answer_rewrite = get_immo_rewrite(ad_desc, template_immo_rewrite)
            st.subheader(rewrite_message)
            st.write(answer_rewrite)

            immo_rewrite_time = time.time()
            logging.info(f"Immo Rewrite - {calculate_time(immo_places_time, immo_rewrite_time)}")

    else:

        st.info(please_desc_message)
