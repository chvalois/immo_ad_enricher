import os
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def extract_elements_from_pdf(filepaths):
    """ extract elements from pdf with partition_pdf"""

    documents = []

    pdf_files = [file for file in os.listdir(filepaths) if file.endswith('.pdf')]
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

    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not neccesary
    )

    pass
