import os
import time
import logging
from bs4 import BeautifulSoup

from dotenv import load_dotenv

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import BSHTMLLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings


load_dotenv()

USER_AGENT = os.getenv('USER_AGENT')
MODEL_OPENAI = os.getenv('MODEL_OPENAI')

from examples import input_ad1, input_ad2, input_wrong1, input_wrong2, output_ad1, output_ad2, output_wrong1, output_wrong2

def get_ad_content(url):
    loader = WebBaseLoader(url)

    pages = []
    for doc in loader.lazy_load():
        pages.append(doc)

    # Parser le HTML et filtrer les parties indésirables avec BeautifulSoup
    soup = BeautifulSoup(pages[0].page_content, "html.parser")

    # Sélectionner les parties spécifiques, par exemple un article
    content = soup.select_one("div")  # Sélecteur CSS qui correspond au contenu principal

    # Récupérer le texte de la partie sélectionnée
    if content:
        page_text = content.get_text()

    print(soup)
    title = pages[0].metadata['title']
    description = pages[0].metadata['title']

    return title, description, page_text

def get_db_vectorstore():

    examples = [
        {"context": input_ad1, "output": output_ad1},
        {"context": input_ad2, "output": output_ad2},
        {"context": input_wrong1, "output": output_wrong1},
        {"context": input_wrong2, "output": output_wrong2},
    ]

    to_vectorize = [" ".join(example.values()) for example in examples]
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=examples)

    example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=3,
    )

    return vectorstore, example_selector

def get_immo_xy_gpt4_fewshots(ad, template) :

    vectorstore, example_selector = get_db_vectorstore()

    # Define the few-shot prompt.
    few_shot_prompt = FewShotChatMessagePromptTemplate(
    # The input variables select the values to pass to the example_selector
        input_variables=["context"],
        example_selector=example_selector,
        example_prompt=ChatPromptTemplate.from_messages(
            [("human", "{context}"), ("ai", "{output}")]
        ),
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            few_shot_prompt,
            ("human", "{context}"),
        ]
    )

    parser = StrOutputParser()

    chain = final_prompt | ChatOpenAI(model=MODEL_OPENAI, temperature=1.0) | parser

    answer = chain.invoke({"context": ad})

    return answer

def get_response(ad, template):
        
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            ("human", "{context}"),
        ]
    )

    parser = StrOutputParser()

    chain = prompt | ChatOpenAI(model=MODEL_OPENAI, temperature=1.0) | parser

    answer = chain.invoke({"context": ad})

    return answer