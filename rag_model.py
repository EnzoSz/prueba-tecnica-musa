# Importar librerías
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.llms.ollama import Ollama
import ollama

# Clase del RAG
class RagModel:
    # Constructor
    def __init__(self, documents_path):
        self.documents_path = documents_path
        self.llm = Ollama(model='llama3', temperature=0)
        self.chunk = self.load_pdf()
        self.embeddings = OllamaEmbeddings(model='llama3')
        self.vectorstore = Chroma.from_documents(self.chunk, self.embeddings)
        self.retriever = self.vectorstore.as_retriever()
    
    # Función de LLM

    def ollama_llm(self, question, context):
        formatted_prompt = f"Q: {question}\n\nContexto(responde solo sobre el contexto entregado): {context}"
        response = ollama.chat(model= 'llama3',
                               messages=[{'role': 'user', 'content': formatted_prompt}],
                               options={'temperature': 0.7, 'max_tokens': 256},
                               )
        return response['message']['content']
    # Función de Carga de PDF
    def load_pdf(self):
        loader = PyPDFLoader(self.documents_path)
        paginas = loader.load()
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=500, 
            chunk_overlap=50,
            length_function=len
        )
        docs = text_splitter.split_documents(paginas)
        return docs

    # Función para combinar los documentos
    def combine_docs(self, docs):
        return '\n\n'.join(doc.page_content for doc in docs)
    
    # Funcion para formar la consulta
    def rag_chain(self, question):
        retrieved_docs = self.retriever.get_relevant_documents(question)
        formatted_context = self.combine_docs(retrieved_docs)

        return self.ollama_llm(question, formatted_context)
