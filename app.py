import streamlit as st
import logging

from llm import get_immo_xy_gpt4_fewshots, get_ad_content, get_immo_review, get_immo_rewrite, get_immo_places
from prompts import template_immo_gps, template_immo_review, template_immo_rewrite, template_immo_places
from utils import generate_polygon_on_map, extract_reviews, display_radar, extract_list, get_gps_coordinate, get_ad_with_gps

st.cache_data.clear()
st.cache_resource.clear()

#### ---- Logging ---- ####

logging.basicConfig(filename='app.log',   # Log file name
                    filemode='w',         # 'w' to overwrite, 'a' to append
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
                    level=logging.INFO)   # Set the log level

st.title("Immo Ad Analyzer")

# URL de l'annonce à parser
ad_url = st.text_input("Renseigner l'URL de l'annonce")

# Description de l'annonce
ad_desc = st.text_area("Copier / Coller ici la description de l'annonce. Inclure impérativement la ville.")

if st.button("Lancer l'analyse"):

    if ad_url:
        title, description, page_text = get_ad_content(ad_url)
        st.subheader(title)
        st.write(description)
        st.write(page_text)

    elif ad_desc:
        
        with st.spinner('Veuillez patienter ..'):
            answer_review = get_immo_review(ad_desc, template_immo_review)
            st.subheader("Review du bien immobilier")

            reviews = extract_reviews(answer_review)
            fig = display_radar(reviews)
            st.plotly_chart(fig)
            st.write(answer_review)

        with st.spinner('Veuillez patienter ..'):
            answer_places = get_immo_places(ad_desc, template_immo_places)
            places_gps, ad_desc_improved = get_ad_with_gps(ad_desc, answer_places)
            st.write(places_gps)

            answer_gps = get_immo_xy_gpt4_fewshots(ad_desc_improved, template_immo_gps)

            st.subheader("Coordonnées probables du bien immobilier")
            fig = generate_polygon_on_map(answer_gps)
            st.plotly_chart(fig)
            st.write(answer_gps)

        with st.spinner('Veuillez patienter ..'):
            answer_rewrite = get_immo_rewrite(ad_desc, template_immo_rewrite)
            st.subheader("Réécriture de l'annonce")
            st.write(answer_rewrite)
