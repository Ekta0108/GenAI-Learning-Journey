# 🧠 Lesson 1: Foundations of Generative AI

This document summarizes the core concepts, diagrams, and hands-on learnings from lessons 1.1 to 1.3 of the Generative AI learning journey.

---

## 📘 Lesson 1.1 – What is Generative AI?

### 🔍 Core Idea:

Generative AI refers to models that create new content (text, images, code, etc.) rather than just analyzing or classifying existing data.

### 💡 Key Concepts:

* **AI**: Making machines smart
* **ML**: Learning from data
* **GenAI**: Creating new data (e.g., text, image)
* **LLMs**: Large Language Models trained on massive text data (e.g., GPT-3.5, GPT-4)

### ✅ Real-World GenAI Examples:

| Task                          | GenAI? | Reason                           |
| ----------------------------- | ------ | -------------------------------- |
| Writing an essay              | ✅ Yes  | Generates new text               |
| Sorting emails as spam        | ❌ No   | Classification task              |
| Generating Python code        | ✅ Yes  | Generates code based on patterns |
| Recommending YouTube videos   | ❌ No   | Recommendation system            |
| Creating a song from a prompt | ✅ Yes  | Composing new music = generation |

### 🔨 Hands-On:

Used Azure OpenAI `ChatCompletion.create()` with system and user messages to generate text.

### 📦 Code Sample:

```python
response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about clouds."}
    ]
)
```

---

## 📘 Lesson 1.2 – How LLMs Generate Text Word by Word

### 🔍 Core Idea:

LLMs like GPT generate text by predicting the **next token** (word or part of a word) one step at a time.

### 🔁 Process Flow:

1. Input → "Tell me a joke about clouds."
2. Tokenization → Break into tokens
3. Context Understanding → Neural network encodes meaning
4. Probability Distribution → Predicts likely next tokens
5. Sampling → Picks next token based on temperature
6. Repeat → Until stop condition (e.g., end-of-sentence)

### 🔤 What is a Token?

* A word or word fragment (e.g., "artificial" or "un" + "believable")
* GPT models don’t generate whole sentences at once, only **token-by-token**

### 🔧 Temperature Explained:

| Temperature | Behavior        |
| ----------- | --------------- |
| 0.0         | Deterministic   |
| 0.5         | Balanced/random |
| 1.0         | Creative/random |

### 🔨 Hands-On:

Experimented with different temperature values to see creativity in model outputs.

---

## 📘 Lesson 1.3 – Prompt Engineering

### 🔍 Core Idea:

The way you write prompts affects how well the model understands and responds.

### 🔑 Prompting Styles:

| Type             | Description                              |
| ---------------- | ---------------------------------------- |
| Zero-shot        | Direct task, no examples                 |
| Few-shot         | Show examples first                      |
| Chain-of-thought | Ask the model to reason step by step     |
| Role prompting   | Define behavior via the "system" message |

### 🔨 Hands-On:

Tried prompts with different roles, examples, and reasoning requests.

### 🔧 Code Pattern:

```python
prompt = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Translate this to French: I love coffee."}
]
response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=prompt
)
```

---

✅ End of Lesson 1 Notes. Ready for Lesson 1.4: RAG vs Fine-Tuning!
