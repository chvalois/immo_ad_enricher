import streamlit as st
import logging
import openai

from llm import get_immo_xy_gpt4_fewshots, get_ad_content, get_response
from prompts import template_immo_gps, template_immo_review, template_immo_rewrite
from utils import generate_polygon_on_map, extract_reviews, display_radar

#### ---- Logging ---- ####

logging.basicConfig(filename='app.log',   # Log file name
                    filemode='w',         # 'w' to overwrite, 'a' to append
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
                    level=logging.INFO)   # Set the log level

st.title("Immo Ad Enricher")


# URL de l'annonce à parser
ad_url = st.text_input("Renseigner l'URL de l'annonce")

# Description de l'annonce
ad_desc = st.text_area("Copier / Coller ici la description de l'annonce. Inclure impérativement la ville.")

if st.button("Lancer l'enrichissement"):

    if ad_url:
        title, description, page_text = get_ad_content(ad_url)
        st.subheader(title)
        st.write(description)
        st.write(page_text)

    elif ad_desc:
        pass
        
        with st.spinner('Veuillez patienter ..'):
            try:
                answer_gps = get_immo_xy_gpt4_fewshots(ad_desc, template_immo_gps)
            except openai.error.APIError as e:
                logging.info(f"API error: {e}")
            except openai.error.Timeout as e:
                logging.info(f"Timeout error: {e}")
            except Exception as e:
                logging.info(f"General error: {e}")

        #     st.subheader("Coordonnées probables du bien immobilier")
        #     fig = generate_polygon_on_map(answer_gps)
        #     st.plotly_chart(fig)
        #     st.write(answer_gps)

        # with st.spinner('Veuillez patienter ..'):
        #     answer_review = get_response(ad_desc, template_immo_review)
        #     st.subheader("Review du bien immobilier")

        #     reviews = extract_reviews(answer_review)
        #     fig = display_radar(reviews)
        #     st.plotly_chart(fig)
        #     st.write(answer_review)

        # with st.spinner('Veuillez patienter ..'):
        #     answer_rewrite = get_response(ad_desc, template_immo_rewrite)
        #     st.subheader("Réécriture de l'annonce")
        #     st.write(answer_rewrite)
