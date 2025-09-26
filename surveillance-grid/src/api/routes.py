from flask import Blueprint, request, jsonify
from src.llm.model import generate_response

api = Blueprint('api', __name__)

@api.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({'error': 'Query is required'}), 400
    
    response = generate_response(user_query)
    
    return jsonify({'response': response})