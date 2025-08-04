# 🧠 Generative AI & AI Agents Learning Journey

This repo documents my hands-on learning of Generative AI & AI Agent concepts, using Python + Azure OpenAI.

---

## ✅ Lessons Completed

### Lesson 1: Foundations of GenAI
- [x] 1.1 What is Generative AI?
- [x] 1.2 How LLMs Generate Text (word-by-word prediction)
- [x] 1.3 Prompt Engineering (Zero-shot, Few-shot, CoT, Role prompting)

### Lessons Coming Up
- [ ] 1.4 Fine-Tuning vs RAG
- [ ] 2.x AI Agents (with tools and memory)
- [ ] Capstone Project

---

## 📂 Folder Structure

- `lessons/`: step-by-step Python exercises
- `docs/`: explanations, visual notes, diagrams
- `scripts/`: sandbox tests (not part of main curriculum)
- `requirements.txt`: Python packages
- `.env`: API keys (not committed)

---

## 📜 Requirements
```bash
pip install -r requirements.txt

### How to Run a Lesson Script
```bash

python lessons/lesson1_3_prompt_engineering.py



## 🔐 Azure OpenAI Setup

To run the lessons, you'll need to set up Azure OpenAI. Follow these steps:

### 1. Create Azure OpenAI Resource
1. Go to [Azure Portal](https://portal.azure.com)
2. Create a new Azure OpenAI resource
3. Deploy a model (GPT-3.5 Turbo recommended)
4. Note down your endpoint URL and API key

### 2. Environment Configuration
Create a `.env` file in the root folder with the following variables:

```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_OPENAI_API_KEY=<your-key>
AZURE_OPENAI_DEPLOYMENT=gpt35turbo
AZURE_OPENAI_API_VERSION=2023-07-01-preview
```

### 3. Get Your Credentials
- **Endpoint**: Found in your Azure OpenAI resource overview
- **API Key**: Available in the "Keys and Endpoint" section
- **Deployment**: The name you gave your model deployment
- **API Version**: Use the latest stable version (2023-07-01-preview)

### 4. Security Note
⚠️ **Important**: Never commit your `.env` file to version control. It's already added to `.gitignore` to prevent accidental commits.
