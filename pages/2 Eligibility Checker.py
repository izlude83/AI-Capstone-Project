# Set up and run this Streamlit App
import streamlit as st
from functions import worker2 


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Find Out Whether You Qualify for the Silver Support Scheme")

option1 = st.selectbox("I am ", ["a Singapore Citizen","not a Singapore Citizen"])
option2 = st.selectbox("My age is ",["65 or above","below 65"])
option3 = st.selectbox("My total CPF contribution is ",["$140,000 or less","more than $140,000"])
option4 = st.selectbox("I ",["stay in a HDB flat","do not stay in a HDB flat"])
option5 = st.selectbox("I ",["own private or multiple properties","do not own private or multiple properties"])
option6 = st.selectbox("My household has a monthly income per person of ",["$1,800 or below","more than $1,800"])

if (st.button("Run")):
   st.toast(f"User Input Submitted")
   user_prompt = "I am " + option1 + ". My age is " + option2 + ". My total CPF contribution is " + option3 + ". I " + option4 + ". I " + option5 + ". My household has a monthly income per person of " + option6 + ". Do I qualify for the Silver Support Scheme?"
   response = worker2.process_user_query(user_prompt)
   st.write(response)
   print(f"User Input is {user_prompt}")

