from flask import request, app
from docs_scan_accessor import DocsScanAccessor
from prompt_generator import PromptGenerator
from response_generator import ResponseGenerator

prompt_generator = PromptGenerator()
docs_accessor = DocsScanAccessor()
response_generator = ResponseGenerator()
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['prompt']
    tenant_id = request.json['tenantId']
    docs = docs_accessor.retrieve_scan_docs(tenant_id, user_input)
    prompt = PromptGenerator().generate_prompt(user_input, docs)
    return ResponseGenerator().get_generated_response(prompt)
