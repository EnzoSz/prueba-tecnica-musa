import unittest
import json 
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 
        
    def test_response(self):
        response = self.app.get('/response',
                                data= json.dumps({'question': '¿Que es un objeto?'}),
                                content_type='application/json')
        
        self.assertEqual(response.status_code, 200, 'El codigo de respuesta no es 200')
        data = json.loads(response.data)
        self.assertIn('response', data, 'La clave response no esta en la respuesta')
        self.assertIsInstance(data['response'], str, 'La respuesta no es un string')
        self.assertGreater(len(data['response']), 0, 'La respuesta es vacia')
        
if __name__ == '__main__':
    unittest.main()