from langchain import OpenAI
class ResponseGenerator:
    def __init__(self):
        self.openai = OpenAI(openai_api_key="")

    def get_generated_response(self, prompt_string:str)->str:
        llm_chain:LLMResult = self.openai.generate(prompts=[prompt_string], max_tokens=64, temperature=0, top_p=1, frequency_penalty=0, presence_penalty=0)
        return llm_chain.generations[0][0].text