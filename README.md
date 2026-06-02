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

# Summary of Findings

This project investigated the effectiveness of different Natural Language Processing (NLP) approaches for intent classification using the CLINC150 dataset, which contains 150 in-domain intents and one Out-of-Scope (OOS) class.

Three models representing different generations of NLP techniques were implemented and evaluated:

| Model                        | Feature Representation            | Validation Accuracy |
| ---------------------------- | --------------------------------- | ------------------: |
| Logistic Regression          | TF-IDF                            |              87.45% |
| Multi-Layer Perceptron (MLP) | TF-IDF                            |              85.97% |
| DistilBERT                   | Contextual Transformer Embeddings |              94.58% |

The classical machine learning baseline using TF-IDF and Logistic Regression achieved strong performance with a validation accuracy of 87.45%, demonstrating that simple lexical representations remain effective for intent classification tasks. The MLP model did not provide a significant improvement over Logistic Regression, suggesting that the TF-IDF feature space was already largely separable and that additional neural network complexity offered limited benefit.

The transformer-based DistilBERT model achieved the best performance with a validation accuracy of 94.58% and a test accuracy of 87.84%. The results demonstrate the advantage of contextual language representations over traditional bag-of-words approaches. By leveraging transfer learning and contextual embeddings, DistilBERT was able to capture semantic relationships that TF-IDF-based models could not represent effectively.

Analysis of the classification report showed strong overall performance, with weighted precision, recall, and F1-scores of 0.90, 0.88, and 0.87 respectively. Macro-average metrics further indicated that the model generalized reasonably well across different intent categories.

Confusion matrix analysis revealed that the majority of errors were associated with the Out-of-Scope (OOS) class. Many OOS utterances were incorrectly mapped to semantically related in-domain intents such as "smart_home", "weather", and "schedule_maintenance". Among in-domain intents, the most common confusions occurred between closely related categories that shared similar vocabulary and semantic meaning.

Manual error analysis confirmed that most misclassifications were not random. Instead, the model typically confused intents belonging to the same domain or addressing similar user needs. Examples included confusion between transfer-related and income-related banking intents, payday and bill-related intents, as well as replacement-card and new-card requests. These findings suggest that the model successfully learned domain-level semantics but occasionally struggled to distinguish between highly similar intent definitions.

Overall, this study demonstrates the progression from classical NLP methods to modern transformer-based architectures. While TF-IDF combined with Logistic Regression provided a strong baseline, transformer models delivered substantially better language understanding and intent recognition capabilities. The results highlight the importance of contextual embeddings in modern NLP systems and show that transfer learning can significantly improve performance on intent classification tasks.

Future work could explore improved Out-of-Scope detection, confidence-based rejection mechanisms, hard-negative sampling strategies, and the evaluation of larger transformer architectures such as BERT or RoBERTa to further enhance performance.
