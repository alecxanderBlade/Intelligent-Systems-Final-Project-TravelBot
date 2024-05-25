from dotenv import load_dotenv

load_dotenv()  

import streamlit as st
import os

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A")

st.header("🛫TravelBot Travel Companion🛬")

input=st.text_input("Where would youn like to travel?: ",key="input")
act_txt=st.text_input("Can you tell me what activities your are going to be doing in " + input + "?", key="act_txt")
budget_amount = st.selectbox(
    'How much is your budget for this trip in Php?',
    (10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000))
submit=st.button("Submit")

if submit:
  response=get_gemini_response("What can I do in " + input + " with a budget of " + "Php" + str(budget_amount) + " while " + act_txt + ". Show me some suggestions on what to do also.")
  st.subheader("A trip to " + input + " while " + act_txt + " with a budget of " + "Php" + str(budget_amount) + " would be a great idea. Here are some suggestions: ")
  st.write(response)
      


