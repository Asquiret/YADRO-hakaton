import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# df = pd.read_csv('pages/titanic.csv')

with st.sidebar:
    st.title('🦙💬 Llama 2 Chatbot')
    st.write('This chatbot is created using the open-source Llama 2 LLM model from Meta.')

st.title("Инфографика с Титаника")

user_name = st.text_input("Как вас зовут?")

if st.button("Приветствовать!"):
    if user_name:
        st.write(f"Привет, {user_name}! Рад тебя видеть на моей странице.")
    else:
        st.write("Пожалуйста, введите ваше имя.")

age = st.slider("Сколько вам лет?", 0, 100, 25)
st.write(f"Вам {age} лет.")

st.markdown("---")  # Горизонтальная линия
st.write("Это простое приложение демонстрирует возможности Streamlit.")
