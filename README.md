# UfanUtom

**UfanUtom** is a multitenant backend platform that empowers organizations to interact with their private data using Retrieval-Augmented Generation (RAG) models. It enables clients to ask natural language questions and receive contextual, data-grounded answers — helping them make smarter business decisions with ease.

## 🚀 Features

- 🔐 **Multitenancy architecture** using schema-based isolation with Django Tenants
- 🧠 **RAG pipeline** for natural language querying over client-specific data
- 📊 **Business intelligence** through conversational interfaces
- 🗂️ **Data ingestion** for structured and unstructured sources
- ⚙️ **Tenant onboarding** and provisioning workflows
- 🧪 **Modular use case and service architecture** with dependency injection
- 🐜 **Load testing** with Locust
- 🧵 **Performance profiling** with Silk

## 🛠️ Tech Stack

- Python 3.11
- Django
- Django Tenants
- PostgreSQL (schema-based multitenancy)
- LangChain / LlamaIndex (for RAG)
- OpenAI / HuggingFace Transformers
- DynamoDB (optional for metadata)
- Pydantic
- Locust
- Silk
- Dependency Injector

## 📦 Installation

```bash
git clone https://github.com/your-username/ufanutom.git
cd ufanutom
pip install -r requirements.txt


## 🧠 How It Works

- **Tenant Onboarding**: Each client is provisioned with a unique schema and isolated data environment.

- **Data Ingestion**: Clients upload structured or unstructured data into their tenant space.

- **RAG Pipeline**: Natural language queries are processed using retrieval + LLM generation.

- **Insight Delivery**: Clients receive contextual answers grounded in their own data.
