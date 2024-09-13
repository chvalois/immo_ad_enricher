import os
import argparse
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

MODEL_EMBEDDING = os.getenv('MODEL_EMBEDDING')

def extract_elements_from_pdf(filepaths, collection_name):
    """
    Génère une base de données de vecteurs à partir de fichiers PDF

    Paramètres
    -------
    filepaths : str | emplacement des fichiers à 'embedder'
    collection_name : str | nom identifiant la base de données
    
    Retourne
    -------
    Rien

    """ 

    documents = []

    pdf_files = [os.path.join(filepaths, file) for file in os.listdir(filepaths) if file.endswith('.pdf')]
    print(pdf_files)

    for pdf_path in pdf_files:

        # Extract text using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                extracted_text = ""
                page_text = page.extract_text()

                extracted_text += page_text + "\n"
                
                # Split text using LangChain's RecursiveCharacterTextSplitter
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                chunks = text_splitter.split_text(extracted_text)
                
                # Wrap each chunk in a Document object with metadata
                for chunk in chunks:
                    # Extract names from the text
                    doc = Document(
                        page_content=chunk,
                        metadata={"page": i + 1, "source": pdf_path}
                    )
                    documents.append(doc)

                    print(doc)
                    print('\n\n')

    embeddings = OpenAIEmbeddings(model=MODEL_EMBEDDING)

    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=f"./chroma_db/{collection_name}"
    )

    # Add documents to the vector store
    vectorstore.add_documents(documents)

    # Optionally, check the number of documents added
    print(f"Number of documents in the vector store: {len(documents)}")

# Create an argument parser
def main():
    """
    Appelle la fonction "extract_elements_from_pdf" en ligne de commande avec arguments

    Arguments
    -------
    filepath : str | emplacement des fichiers à 'embedder'
    collection_name : str | nom identifiant la base de données
    """ 

    parser = argparse.ArgumentParser(description='Function to fill a Chroma DB with PDF documents content.')
    parser.add_argument('--filepath', type=str, required=True, help='Filepath of the PDF documents')
    parser.add_argument('--collection_name', type=str, required=True, help='Collection Name for the Chroma DB')
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call your function with the arguments
    extract_elements_from_pdf(args.filepath, args.collection_name)

# Ensure the script runs when executed with python -m
if __name__ == "__main__":
    main()