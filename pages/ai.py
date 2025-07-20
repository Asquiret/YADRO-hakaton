import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

# API Configuration

LKEY = "sk-GCa0Lb_wCVjbOf2Nma3vOYJjhp6VgCD3B-4QOKqXYTo"
url = "http://localhost:7860/api/v1/run/21f98a82-0b30-47e4-9b38-001c189099bf"  # The complete API endpoint URL for this flow

def ask_bot(question):
    # Request payload configuration
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": "hello world!"
    }

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "x-api-key": LKEY  # Authentication key from environment variable
    }

    try:
        # Send API request
        response = requests.request("POST", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        # Print response
        print("RESPONSE!!")
        a = json.loads(response.text)
        print(a)
        #answer = a["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
        return(a)

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except ValueError as e:
        print(f"Error parsing response: {e}")

st.header("Общение с AI-ботом")

prompt = st.text_input("Задайте вопрос боту:")

if (prompt):
    ans = ask_bot(prompt)
    st.markdown(ans)

# if st.button("Отправить"):
#     answer = ask_bot(question)
#     st.write("Ответ бота:")
#     st.write(answer)
