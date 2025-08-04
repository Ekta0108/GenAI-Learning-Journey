import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Load env variables
load_dotenv()

# Set OpenAI credentials
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
os.environ["OPENAI_API_VERSION"] = os.getenv("AZURE_OPENAI_API_VERSION")

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Step 1: Load PDF
loader = PyPDFLoader("docs/sample.pdf")
pages = loader.load()

# Step 2: Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
chunks = splitter.split_documents(pages)

# Step 3: Create vector store (Chroma) using embeddings
embedding = OpenAIEmbeddings(deployment=deployment_name)
vectorstore = Chroma.from_documents(chunks, embedding)

# Step 4: Build Retrieval-based QA chain
llm = AzureChatOpenAI(deployment_name=deployment_name, temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# Step 5: Ask a question
query = "Summarize the key topics in this document."
result = qa.run(query)
print("\n📄 Answer:", result)
