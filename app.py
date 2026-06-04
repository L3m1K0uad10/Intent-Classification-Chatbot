import streamlit as st

from predict import predict_intent
from utils import (
    get_actions_by_intent,
    get_chat_response
)


# sidebar configuration and metrics
with st.sidebar:
    st.header("Model Statistics")
    st.markdown("---")
    
    # model Metadata
    st.metric(label = "Architecture Engine", value = "DistilBERT")
    st.metric(label = "Supported Intents", value = "151 Classes")
    
    st.markdown("---")
    st.subheader("Benchmark Accuracy")
    
    # styled metrics for performance metrics
    col_val, col_test = st.columns(2)
    with col_val:
        st.metric(label = "Validation", value = "94.58%")
    with col_test:
        st.metric(label = "Test", value = "87.84%")
        
    st.markdown("---")
    st.caption("Trained on the CLINC150 out-of-scope variant dataset pipeline.")


# setting the app title
st.title("Intent Classification Assistant")
st.markdown("Type a message or select an example below to analyze underlying intents and route suggested hooks.")

# initializing Session States for persistent tracking across button clicks
if "current_intent" not in st.session_state:
    st.session_state.current_intent = None
if "confidence" not in st.session_state:
    st.session_state.confidence = 0.0
if "top_predictions" not in st.session_state:
    st.session_state.top_predictions = []
if "selected_action" not in st.session_state:
    st.session_state.selected_action = None
if "input_text_value" not in st.session_state:
    st.session_state.input_text_value = ""


# interactive example queries
st.subheader("Try an Example Query")
example_cols = st.columns(3)

examples = [
    "Move fifty dollars from savings to checking.",
    "What's the forecast for tomorrow?",
    "Why is the sky blue?"
]

# When an example is clicked, inject it directly into the input state memory
for idx, example in enumerate(examples):
    with example_cols[idx]:
        if st.button(f'"{example}"', key = f"ex_{idx}"):
            st.session_state.input_text_value = example
            
            # clearing previous intent selections to fetch a fresh cycle
            st.session_state.current_intent = None
            st.session_state.selected_action = None
            st.rerun()


# prediction logic loop

# creating an input field for the user to enter a message
# e.g message: How much money can I transfer today?
user_text = st.text_input(
    "Enter a message",
    value = st.session_state.input_text_value,
    placeholder = "Type something here..."
)

col_predict, col_clear = st.columns([1, 5])
with col_predict:
    predict_clicked = st.button("Predict Intent", type = "primary")
with col_clear:
    if st.button("Clear Cache"):
        st.session_state.current_intent = None
        st.session_state.confidence = 0.0
        st.session_state.top_predictions = []
        st.session_state.selected_action = None
        st.session_state.input_text_value = ""
        st.rerun()

# executing model assessment if explicitly clicked
if predict_clicked and user_text:
    # fetching the predicted intent, confidence score, and top predictions from the model
    intent, confidence, top_predictions = predict_intent(user_text)
    
    # saving parameters securely to the memory state
    st.session_state.current_intent = intent
    st.session_state.selected_action = None 
    st.session_state.confidence = confidence
    st.session_state.top_predictions = top_predictions



# persistent display rendering 
if st.session_state.current_intent:
    intent = st.session_state.current_intent
    confidence = st.session_state.confidence
    top_predictions = st.session_state.top_predictions

    st.markdown("---")
    
    # layout Split: Left side shows stats, right side shows Chat/Actions UI
    main_col, side_col = st.columns([3, 2])
    
    with main_col:
        st.subheader("Assistant Response")
        
        # fetching dynamic reply from dictionary
        reply_text = get_chat_response(intent)
        with st.chat_message("assistant"):
            st.write(reply_text)
            
        # suggested Actions 
        suggested_actions = get_actions_by_intent(intent)
        if suggested_actions:
            st.markdown(" ")
            st.caption("Suggested actions:")
            
            # drawing action blocks dynamically inside variable column grids
            action_cols = st.columns(len(suggested_actions))
            for idx, action in enumerate(suggested_actions):
                with action_cols[idx]:
                    # formatting the action name to be more human readable for the button label
                    button_label = action.replace("_", " ").title()

                    # when an action button is clicked, save the selection to memory and trigger the confirmation overlay
                    if st.button(button_label, key = f"act_{action}_{idx}"):
                        st.session_state.selected_action = button_label
                        st.rerun()
    
    # side column for analytics summary and details
    with side_col:
        st.subheader("Analytics Summary")
        st.markdown(f"**Predicted Intent:** `{intent}`")
        st.markdown(f"**Confidence Score:** {confidence:.2%}")
        st.progress(confidence)
        
        with st.expander("View Classification Array Details"):
            for label, score in top_predictions:
                st.text(f"{label:<22} {score:.2%}")


# action confirmation and trigger simulation
if st.session_state.selected_action:
    st.markdown("---")
    st.success(f"⚡ **Backend Automation Triggered:** Instantiated automated infrastructure pipeline scripts for **{st.session_state.selected_action}**.")