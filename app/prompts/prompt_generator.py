from langchain.prompts import Prompt, PromptTemplate
from langchain.schema import Document
import json

class PromptGenerator:
    def __init__(self):
        with open('./app/prompts/prompt_template.md') as prompt_template_file:
            self.template = prompt_template_file.read()

    def generate_prompt(self, user_input:str, documents:[Document]) -> Prompt:
        sources = []
        for doc in documents:
            source = json.loads(doc.page_content)
            sources.append({"Answer":source['Answer']})
        prompt_template = PromptTemplate(input_variables=["Question", "Docs"], template=self.template)
        return prompt_template.format(Question=user_input, Docs=sources)

