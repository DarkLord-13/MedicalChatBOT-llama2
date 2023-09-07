from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings # if u get error, replace it with sentence transformer
from langchain.vectorstores import FAISS

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss' 

# create vector DB
def create_vector_db():
    
    loader = DirectoryLoader(DATA_PATH, # DATA_PATH specifies the path from where we will input our data
                             glob = '*.pdf', # since our input documents are in pdf format, we use PyPDFLoader, and give extensions as .pdf in glob
                             loader_cls = PyPDFLoader
                             ) 
    documents = loader.load() # loaded documents are stored in the documents variable, as a list of objects
    
    text_splitter = RecursiveCharacterTextSplitter(
                            chunk_size=500, # chunk_size -> specifies the number of tokens per list
                            chunk_overlap=50 # chunk_overlap -> how much overlap is taking place between start and end (sliding window concept)
                            )
        
    texts = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs = {'device':'cpu'})
    
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)
    
if __name__ == '__main__':
    create_vector_db()