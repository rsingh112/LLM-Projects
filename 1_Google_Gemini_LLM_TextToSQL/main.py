from SuperStoreModelLLM import get_result
import streamlit as st


st.title("SuperStore Data ChatBot!!!")
question = st.text_input("Question: ")

if question:
    answer = get_result(question)
    st.header("Answer: ")
    st.write(answer)