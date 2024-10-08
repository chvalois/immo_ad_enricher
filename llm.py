import os

from bs4 import BeautifulSoup

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
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from dotenv import load_dotenv
load_dotenv()

MODEL_OPENAI = os.getenv('MODEL_OPENAI')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_EMBEDDING = os.getenv('MODEL_EMBEDDING')

from examples import input_ad1, input_ad2, input_ad3, output_ad1, output_ad2, output_ad3, input_wrong1, input_wrong2, input_wrong3,  \
output_wrong1, output_wrong2, output_wrong3, output_immoreview_ad1, output_immoreview_ad2, input_places_ad1, input_places_ad2, \
output_places_ad1, output_places_ad2

from examples_EN import input_ad1_EN, input_ad2_EN, input_ad3_EN, output_ad1_EN, output_ad2_EN, output_ad3_EN, input_wrong1_EN, input_wrong2_EN, input_wrong3_EN,  \
output_wrong1_EN, output_wrong2_EN, output_wrong3_EN, output_immoreview_ad1_EN, output_immoreview_ad2_EN, input_places_ad1_EN, input_places_ad2_EN, \
output_places_ad1_EN, output_places_ad2_EN

def get_db_vectorstore(examples, language, examples_type):
    """
    Génère une base de données de vecteurs à partir d'exemples pour entraîner le modèle LLM

    Paramètres
    -------
    examples : dict
    
    Retourne
    -------
    example_selector : base de données de vecteurs d'exemples pour une réponse de type FewShot du LLM
    """ 

    to_vectorize = [" ".join(example.values()) for example in examples]

    # Ensure that none of the texts are None or empty
    if not to_vectorize or any(not text for text in to_vectorize):
        raise ValueError("The examples contain invalid or empty values.")
    
    embeddings = OpenAIEmbeddings()

    vectorstore = None

    try:
        vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=examples, persist_directory=f"./chroma_db/{examples_type}_{language}")
    except Exception as e:
        print(f"Error creating vectorstore: {e}")

    # Check if vectorstore was created successfully
    if vectorstore is None:
        raise ValueError("Failed to create vectorstore. Please check the logs for details.")

    example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=3,
    )

    return example_selector

def get_immo_xy_gpt4_fewshots(ad, template, language) :
    """
    Retourne la réponse du LLM quant aux coordonnées probables d'un bien immobilier à partir d'une annonce

    Paramètres
    -------
    ad : str
    template : str | prompt utilisé pour générer la réponse
    
    Retourne
    -------
    answer : str
    """ 
    
    if language == 'EN':

        examples = [
        {"input": input_ad1_EN, "output": output_ad1_EN},
        {"input": input_ad2_EN, "output": output_ad2_EN},
        {"input": input_ad3_EN, "output": output_ad3_EN},
        {"input": input_wrong1_EN, "output": output_wrong1_EN},
        {"input": input_wrong2_EN, "output": output_wrong2_EN},
        {"input": input_wrong3_EN, "output": output_wrong3_EN},
    ]
    
    else:

        examples = [
        {"input": input_ad1, "output": output_ad1},
        {"input": input_ad2, "output": output_ad2},
        {"input": input_ad3, "output": output_ad3},
        {"input": input_wrong1, "output": output_wrong1},
        {"input": input_wrong2, "output": output_wrong2},
        {"input": input_wrong3, "output": output_wrong3},
    ]

    example_selector = get_db_vectorstore(examples, language, examples_type="examples_gps")
    # Define the few-shot prompt.
    few_shot_prompt = FewShotChatMessagePromptTemplate(
    # The input variables select the values to pass to the example_selector
        input_variables=["input"],
        example_selector=example_selector,
        example_prompt=ChatPromptTemplate.from_messages(
            [("human", "{input}"), ("ai", "{output}")]
        ),
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            few_shot_prompt,
            ("human", "{input}"),
        ]
    )

    parser = StrOutputParser()

    chain = final_prompt | ChatOpenAI(model=MODEL_OPENAI, temperature=1.0) | parser

    answer = chain.invoke({"input": ad})

    return answer


def get_immo_review(ad, template, language):
    """
    Retourne la réponse du LLM quant à la review de la description du bien immobilier

    Paramètres
    -------
    ad : str
    template : str | prompt utilisé pour générer la réponse
    
    Retourne
    -------
    answer : str
    """ 

    if language == 'EN':

        examples = [
        {"input": input_ad1_EN, "output": output_immoreview_ad1_EN},
        {"input": input_ad2_EN, "output": output_immoreview_ad2_EN},
        {"input": input_wrong1_EN, "output": output_wrong1_EN},
        {"input": input_wrong2_EN, "output": output_wrong2_EN},
        {"input": input_wrong3_EN, "output": output_wrong3_EN},
        ]

        immo_review_db = 'immo_review_EN'

    else:

        examples = [
        {"input": input_ad1, "output": output_immoreview_ad1},
        {"input": input_ad2, "output": output_immoreview_ad2},
        {"input": input_wrong1, "output": output_wrong1},
        {"input": input_wrong2, "output": output_wrong2},
        {"input": input_wrong3, "output": output_wrong3},
        ]        
        
        immo_review_db = 'immo_review'


    example_selector = get_db_vectorstore(examples, language, examples_type="examples_reviews")
    # Define the few-shot prompt.
    few_shot_prompt = FewShotChatMessagePromptTemplate(
    # The input variables select the values to pass to the example_selector
        input_variables=["input"],
        example_selector=example_selector,
        example_prompt=ChatPromptTemplate.from_messages(
            [("human", "{input}"), ("ai", "{output}")]
        ),
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            few_shot_prompt,
            ("human", "{input}"),
        ]
    )

    llm = ChatOpenAI(model=MODEL_OPENAI, temperature=0.3)

    if os.path.exists('./chroma_db/immo_review'):
        print("Chargement de la base de données Chroma existante")
        vectorstore = Chroma(
            persist_directory=f'./chroma_db/{immo_review_db}',
            collection_name=immo_review_db,
            embedding_function=OpenAIEmbeddings(model=MODEL_EMBEDDING)
        )

        print("Nb de documents retrouvés", len(vectorstore.get()['documents']))

    try:
        db_retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

        question_answer_chain = create_stuff_documents_chain(llm, final_prompt)
        rag_chain = create_retrieval_chain(db_retriever, question_answer_chain) 

    except IndexError as e:
        print(f"IndexError: {e}")

    answer = rag_chain.invoke({"input": ad})
    
    return answer['answer']
    

    
def get_immo_rewrite(ad, template):
    """
    Retourne la réponse du LLM quant à la réécriture de la description du bien immobilier

    Paramètres
    -------
    ad : str
    template : str | prompt utilisé pour générer la réponse
    
    Retourne
    -------
    answer : str
    """ 

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            ("human", "{context}"),
        ]
    )

    parser = StrOutputParser()

    llm = ChatOpenAI(model=MODEL_OPENAI, temperature=1)

    chain = prompt | llm | parser
    answer = chain.invoke({"context": ad})

    return answer


def get_immo_places(ad, template, language):
    """
    Retourne la réponse du LLM quant aux lieux identifiés dans la description du bien immobilier

    Paramètres
    -------
    ad : str
    template : str | prompt utilisé pour générer la réponse
    
    Retourne
    -------
    answer : str
    """ 

    if language == 'EN':

        examples = [
        {"input": input_places_ad1_EN, "output": output_places_ad1_EN},
        {"input": input_places_ad2_EN, "output": output_places_ad2_EN},
        {"input": input_wrong1_EN, "output": output_wrong1_EN},
        {"input": input_wrong2_EN, "output": output_wrong2_EN},
        {"input": input_wrong3_EN, "output": output_wrong3_EN},
    ]

    else:

        examples = [
        {"input": input_places_ad1, "output": output_places_ad1},
        {"input": input_places_ad2, "output": output_places_ad2},
        {"input": input_wrong1, "output": output_wrong1},
        {"input": input_wrong2, "output": output_wrong2},
        {"input": input_wrong3, "output": output_wrong3},
    ]


    example_selector = get_db_vectorstore(examples, language, examples_type="examples_places")
    # Define the few-shot prompt.
    few_shot_prompt = FewShotChatMessagePromptTemplate(
    # The input variables select the values to pass to the example_selector
        input_variables=["input"],
        example_selector=example_selector,
        example_prompt=ChatPromptTemplate.from_messages(
            [("human", "{input}"), ("ai", "{output}")]
        ),
    )

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            few_shot_prompt,
            ("human", "{input}"),
        ]
    )

    parser = StrOutputParser()

    llm = ChatOpenAI(model=MODEL_OPENAI, temperature=0.3)

    chain = final_prompt | llm | parser
    answer = chain.invoke({"input": ad})

    return answer

# ----------------------------------

def get_ad_content(url):
    """
    #! Pas utilisé dans le code, à conserver si on souhaite parser le contenu d'une URL
    Renvoie le titre, la description et le contenu d'une URL

    Paramètres
    -------
    url : str
    
    Retourne
    -------
    title : str
    description : str
    page_text : str
    """ 

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