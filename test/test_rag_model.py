import unittest

from rag_model import RagModel

class TestRagModel(unittest.TestCase):
    def setUp(self):
        self.documents_path = 'GuiaPOO2.pdf'
        self.rag_model = RagModel(self.documents_path)

    def test_load_pdf(self):
        chunk = self.rag_model.load_pdf()
        self.assertIsNotNone(len(chunk)), 0, 'No se ha cargado el pdf correctamente o esta vacio'

    def test_combine_docs(self):
        docs= self.rag_model.load_pdf()
        combined_text = self.rag_model.combine_docs(docs)
        self.assertGreater(len(combined_text), 0, 'No se ha combinado el texto correctamente')
    def test_rag_chain(self):
        question = '¿Que es un objeto?'
        response = self.rag_model.rag_chain(question)
        self.assertIsInstance(response, str, 'La respuesta no es un string')
        self.assertGreater(len(response), 0, 'La respuesta es vacia')
        
if __name__ == '__main__':
    unittest.main()