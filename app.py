import streamlit as st

from predict import predict_intent
from utils import (
    get_actions_by_intent,
    get_chat_response
)



# setting the app title
st.title("Intent Classification Assistant")

# initializing Session State variables
# this is like a small memory bank that survives app reruns
if "current_intent" not in st.session_state:
    st.session_state.current_intent = None
if "selected_action" not in st.session_state:
    st.session_state.selected_action = None

# creating an input field for the user to enter a message
# e.g message: How much money can I transfer today?
user_text = st.text_input("Enter a message")

# displaying the entered message
st.write("You entered:")
st.write(user_text)

# adding predict buttons
if st.button("Predict Intent"):
    intent, confidence, top_predictions = predict_intent(user_text)

    # saving to session state
    st.session_state.current_intent = intent
    st.session_state.selected_action = None # this reset any old selected action

    st.subheader("Top Predictions")
    st.success(intent)

    for label, score in top_predictions:
        st.write(f"{label}: {score:.2%}")

    st.progress(confidence)
    st.write(f"Confidence: {confidence:.2%}")

if st.session_state.current_intent:
    intent = st.session_state.current_intent

    # getting a dynamic, randomized string response for the predicted intent
    reply_text = get_chat_response(intent) 
    # displaying the response
    st.chat_message("assistant").write(reply_text)

    # finding the actions using our utility helper function
    suggested_actions = get_actions_by_intent(intent)

    if suggested_actions:
        st.subheader("Suggested Actions")

        cols = st.columns(len(suggested_actions))

        for col, action in zip(cols, suggested_actions):
            with col:
                # cleaning up the action btn label name for better presentation
                button_label = action.replace("_", " ").title()
                
                # when the user clicks on an action button, we save the selected action to session state and trigger a rerun to update the UI
                if st.button(button_label, key = f"btn_{action}"):
                    st.session_state.selected_action = button_label 
                    st.rerun()

if st.session_state.selected_action:
    st.write("---")
    st.subheader("Action Output")
    st.success(f"Successfully triggered backend automation for: **{st.session_state.selected_action}**")
                    






