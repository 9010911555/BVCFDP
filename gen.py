import streamlit as st  
import google.generativeai as genai     
st.title("Google generative AI with Streamlit ")
st.write('my app')
user_input = st.text_input("Enter your prompt here:")
genai.configure(api_key="AIzaSyCvAL_OW_h7_7Oc19_tCx4WMg9lt71n7fk")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)