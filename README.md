# Intent Classification Chatbot: End-to-End NLP System from Classical ML to Transformers

### Description

This project builds an **end-to-end Intent Classification system that can understand user messages and classify them into predefined intents** such as booking a flight, canceling an order, checking account status, or requesting support.

The goal is to simulate the core intelligence behind modern chatbots used in customer service and virtual assistants.

The project follows a complete NLP pipeline, starting from text preprocessing and feature engineering, moving through traditional machine learning models (TF-IDF + Logistic Regression), and extending to Multi-Layer Perceptron MLP model and transformer-based models (DistilBERT).

A full comparison of models is performed to analyze performance trade-offs between accuracy, speed, and complexity. Finally, the best model is deployed in a simple API or chat interface to simulate real-world usage.

</br>

### Dataset Info

Primary Dataset: CLINC150 Intent Classification Dataset

The project uses the CLINC150 dataset, a widely used benchmark dataset for intent classification in conversational AI systems.

**Dataset Overview**:
- Total Intents: 150 different intent classes
- Total Samples: ~23,700 utterances
- Domains Covered: Banking, travel, credit cards, online shopping, utilities, messaging, etc.
- Language: English
- Type: Supervised text classification dataset

### Goal
Build the following models:
```
TF-IDF + Logistic Regression
          ↓
TF-IDF + Neural Network (MLP)
          ↓
BERT Fine-Tuning (DistilBERT)
          ↓
Comparison & Analysis
```