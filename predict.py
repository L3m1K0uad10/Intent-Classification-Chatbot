import torch

import pickle

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)


# loading the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("model")
model = AutoModelForSequenceClassification.from_pretrained("model")

model.eval()

# loading the label mapping
with open("label_mapping.pkl", "rb") as f:
    label_names = pickle.load(f)


# prediciton function
def predict_intent(text):
    """  
    Predicts the intent of a given text input.
    Args:
        text (str): The input text for which to predict the intent.
    Returns:
        tuple: A tuple containing the predicted intent, confidence score, and top 3 predictions with their probabilities.
    """
    inputs = tokenizer(
        text,
        return_tensors = "pt",
        truncation = True,
        padding = True
    )

    with torch.no_grad():

        # removing token_type_ids if it exists because DistilBERT does not use them
        inputs.pop("token_type_ids", None)

        outputs = model(**inputs)

        # retrieving the probabilities
        probs = torch.softmax(outputs.logits, dim = 1)

    pred_idx = probs.argmax().item()
    confidence = probs.max().item()

    # retrieving the top 3 predictions
    top_probs, top_indices = torch.topk(probs, k = 3)

    top_predictions = []

    # mapping the top indices to their corresponding labels and probabilities
    for p, idx in zip(top_probs[0], top_indices[0]):
        top_predictions.append((label_names[idx.item()], p.item()))

    return (
        label_names[pred_idx],
        confidence,
        top_predictions
    )


""" 
# testing before streamlit: checking if the backbone is working, if prediciton works
intent, confidence = predict_intent(
    "How much money can I transfer today?"
)

print(intent)
print(confidence)
"""