import streamlit as st
import joblib


st.title("Movie Review Sentiment Analyzer")

st.write(
    """
    Welcome to the Movie Review Sentiment Analyzer!  
    The following app predicts whether a movie review is **positive** or **negative**  
    using a Naive Bayes model trained on the IMDB dataset.
    """
)

# Load the trained Model (cached to only load once)
@st.cache_data
def load_model():
    """Load and return the trained sentiment analysis model."""
    return joblib.load("sentiment_model.pkl")

model = load_model()

# User Input: Movie Review to Analyze 
user_review = st.text_area("Enter a movie review to analyze:")

if st.button("Analyze"):
    if user_review.strip():  # make sure input isn’t empty
        # Prediction
        prediction = model.predict([user_review])[0]
        proba = model.predict_proba([user_review])[0]

        if prediction == "positive":
            st.subheader("Predicted Sentiment: Positive")
            st.write(f"Confidence: {proba[1]:.2f}")
        else:
            st.subheader("Predicted Sentiment: Negative")
            st.write(f"Confidence: {proba[0]:.2f}")
    else:
        st.warning("Please enter a review before clicking Analyze.")