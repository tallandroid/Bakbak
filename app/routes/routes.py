from flask import request, app
from app.docs.docs_scan_accessor import DocsScanAccessor
from app.prompts.prompt_generator import PromptGenerator
from app.response_generator import ResponseGenerator

prompt_generator = PromptGenerator()
docs_accessor = DocsScanAccessor()
response_generator = ResponseGenerator()

@app.route('/get_response', methods=['GET'])
def get_response():
    user_input = request.json['user_input']
    tenant_id = request.json['tenantId']
    docs = docs_accessor.retrieve_scan_docs(user_input)
    prompt = prompt_generator.generate_prompt(user_input, docs)
    return response_generator.get_generated_response(prompt)
