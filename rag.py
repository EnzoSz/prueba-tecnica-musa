import pdfplumber
from sentence_transformers import SentenceTransformer, util
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class RAGSystem:
    def __init__(self, document_path,):
        self.document_path = document_path
        self.model = SentenceTransformer('paraphrase-MiniLM-L12-v2')
        self.text_chunks = self.load_and_preprocess_document()
        self.embeddings = self.model.encode(self.text_chunks, convert_to_tensor=True)
        self.tokenizer = AutoTokenizer.from_pretrained("gpt-3.5-turbo")
        self.language_model = AutoModelForCausalLM.from_pretrained("gpt-3.5-turbo")
    
    def load_and_preprocess_document(self):
        with pdfplumber.open(self.document_path) as pdf:
            text= ""
            for page in pdf.pages:
                text += page.extract_text()
        return text.split('\n\n') # Divide el texto en bloques mas pequeños
    
    