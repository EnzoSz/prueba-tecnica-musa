from flask import Flask, request, jsonify
from rag_model import RagModel

app = Flask(__name__)

@app.route('/response', methods=['POST'])

def response():
    data= request.get_json()
    question = data['question']
    if not question:
        return jsonify({'error': 'Missing question'}), 400
    # Inicializamos el modelo RAG
    rag_model = RagModel('GuiaPOO2.pdf')
    response = rag_model.rag_chain(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)