import streamlit as st
import logging
import time
import platform

from llm import get_immo_xy_gpt4_fewshots, get_immo_review, get_immo_rewrite, get_immo_places
from prompts import template_immo_gps, template_immo_review, template_immo_rewrite, template_immo_places
from utils import generate_polygon_on_map, extract_reviews, display_radar, get_ad_with_gps, calculate_time, get_user_agent

if platform.system() == "Linux":
    # Import packages for Linux
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

st.cache_data.clear()
st.cache_resource.clear()

#### ---- Logging ---- ####

logging.basicConfig(filename='app.log',   # Log file name
                    filemode='w',         # 'w' to overwrite, 'a' to append
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
                    level=logging.INFO)   # Set the log level


st.title("Immo Ad Analyzer")

# Description de l'annonce
ad_desc = st.text_area("Copier / Coller ici la description de l'annonce. Inclure impérativement la ville.", height=250)

if st.button("Lancer l'analyse"):

    if ad_desc:

        start = time.time()
        
        with st.spinner('Veuillez patienter ..'):
            logging.info("")
            answer_review = get_immo_review(ad_desc, template_immo_review)
            st.subheader("Review du bien immobilier")

            reviews = extract_reviews(answer_review)
            fig = display_radar(reviews)
            st.plotly_chart(fig)
            st.write(answer_review)

            immo_review_time = time.time()
            logging.info(f"Immo Review - {calculate_time(start, immo_review_time)}")

        with st.spinner('Veuillez patienter ..'):
            answer_places = get_immo_places(ad_desc, template_immo_places)
            places_gps, ad_desc_improved = get_ad_with_gps(ad_desc, answer_places)

            answer_gps = get_immo_xy_gpt4_fewshots(ad_desc_improved, template_immo_gps)

            st.subheader("Coordonnées probables du bien immobilier")
            st.write(places_gps)
            fig = generate_polygon_on_map(answer_gps)
            st.plotly_chart(fig)
            st.write(answer_gps)

            immo_places_time = time.time()
            logging.info(f"Immo Guess GPS - {calculate_time(immo_review_time, immo_places_time)}")

        with st.spinner('Veuillez patienter ..'):
            answer_rewrite = get_immo_rewrite(ad_desc, template_immo_rewrite)
            st.subheader("Réécriture de l'annonce")
            st.write(answer_rewrite)

            immo_rewrite_time = time.time()
            logging.info(f"Immo Rewrite - {calculate_time(immo_places_time, immo_rewrite_time)}")

    else:

        st.info("Veuillez renseigner une description")
