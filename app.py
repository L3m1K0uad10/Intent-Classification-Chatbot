import streamlit as st

from predict import predict_intent



# setting the app title
st.title("Intent Classification Assistant")

# creating an input field for the user to enter a message
# e.g message: How much money can I transfer today?
user_text = st.text_input(
    "Enter a message"
)

# displaying the entered message
st.write("You entered:")
st.write(user_text)

# adding predict buttons
if st.button("Predict Intent"):
    intent, confidence = predict_intent(user_text)

    st.write(f"Intent: {intent}")
    st.write(f"Confidence: {confidence:.2%}")