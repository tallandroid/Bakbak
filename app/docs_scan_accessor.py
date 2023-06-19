from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
class DocsScanAccessor:
    def __init__(self): 
        self.vectorstore = None

    def retrieve_scan_docs(self):
        return None

    def _get_embeddings_from_inputs(self, userInput):
        return None