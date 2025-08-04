import os
from dotenv import load_dotenv

from langchain_community.chat_models import AzureChatOpenAI
from langchain_community.document_loaders import PyPDFLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Load env variables
load_dotenv()

# Set OpenAI credentials
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["azure_endpoint"] = os.getenv("AZURE_OPENAI_ENDPOINT")
os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
os.environ["OPENAI_API_VERSION"] = os.getenv("AZURE_OPENAI_API_VERSION")

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
chat_deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

# Step 1: Load PDF
loader = PyPDFLoader("docs/AZ-500.pdf")
pages = loader.load()

# Step 2: Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=2048, chunk_overlap=200)
chunks = splitter.split_documents(pages)

# Step 3: Create vector store (Chroma) using embeddings
embedding = AzureOpenAIEmbeddings(deployment=deployment_name)
vectorstore = Chroma.from_documents(chunks, embedding)

# Step 4: Build Retrieval-based QA chain
llm = AzureChatOpenAI(deployment_name=chat_deployment_name, temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# Step 5: Ask a question
query = "Summarize the key topics about Azure AD-Identity Protection in this document."
result = qa.run(query)
print("\n Answer:", result)
