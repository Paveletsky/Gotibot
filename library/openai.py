import openai
from llama_index import (StorageContext, load_index_from_storage, 
                         SimpleDirectoryReader, GPTVectorStoreIndex)

class SupportAI():
    def __init__(self, apikey, kgs) -> None:
        openai.api_key = apikey

        docs = SimpleDirectoryReader(kgs).load_data()
        GPTVectorStoreIndex.from_documents(docs).storage_context.persist()

        self.storage = StorageContext.from_defaults(persist_dir='./storage')
        self.index = load_index_from_storage(self.storage)
        self.engine = self.index.as_query_engine()