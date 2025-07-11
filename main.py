#import streamlit as st
#import pandas as pd
#import requests
#from io import BytesIO#

## flask --app api.py run --port=5000
#prediction_endpoint = "http://127.0.0.1:5000/predict"#

#st.title("Text Sentiment Predictor")#

#uploaded_file = st.file_uploader(
#    "Choose a CSV file for bulk prediction - Upload the file and click on Predict",
#    type="csv",
#)#

## Text input for sentiment prediction
#user_input = st.text_input("Enter text and click on Predict", "")#

## Prediction on single sentence
#if st.button("Predict"):
#    if uploaded_file is not None:
#        file = {"file": uploaded_file}
#        response = requests.post(prediction_endpoint, files=file)
#        response_bytes = BytesIO(response.content)
#        response_df = pd.read_csv(response_bytes)#

#        st.download_button(
#            label="Download Predictions",
#            data=response_bytes,
#            file_name="Predictions.csv",
#            key="result_download_button",
#        )#

#    else:
#        response = requests.post(prediction_endpoint, json={"text": user_input})
#        response = response.json()
#        st.write(f"Predicted sentiment: {response['result']}")#
#


# Predict button
import streamlit as st
import requests

st.set_page_config(page_title="Smart Sentiment Analyzer", page_icon="💬")

# Attractive title
st.title("💬 Smart Product Review Sentiment Analyzer")

# User input
review = st.text_area("Write your product review here:")

if st.button("Analyze Sentiment"):
    if review.strip():
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"text": review}
        )
        if response.status_code == 200:
            result = response.json()["result"]
            if result == "Positive":
                st.success(f"✅ Sentiment: **{result}**")
            else:
                st.error(f"❌ Sentiment: **{result}**")
        else:
            st.error("Something went wrong with the API.")
    else:
        st.warning("Please enter a review first.")
