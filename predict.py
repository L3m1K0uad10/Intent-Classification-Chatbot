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

    return (
        label_names[pred_idx],
        confidence
    )


""" 
# testing before streamlit: checking if the backbone is working, if prediciton works
intent, confidence = predict_intent(
    "How much money can I transfer today?"
)

print(intent)
print(confidence)
"""