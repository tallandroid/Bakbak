from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}

class DocsScanAccessor:
    def __init__(self):
        jq_schema = '.[]'
        data = JSONLoader(file_path="./test_dataset.txt", jq_schema=jq_schema, text_content=False)
        self.db = Chroma.from_documents(data.load(), huggingface_embeddings)
        self.huggingface_embeddings = HuggingFaceEmbeddings(
            model_name=model_name, 
            model_kwargs=model_kwargs, 
            encode_kwargs=encode_kwargs)

    def retrieve_scan_docs(self, userInput):
        user_input_embed = self._get_embeddings_from_inputs(userInput)
        return self.db.similarity_search_by_vector(user_input_embed, top_k=5)

    def _get_embeddings_from_inputs(self, userInput):
        return self.huggingface.embed_query(userInput)
