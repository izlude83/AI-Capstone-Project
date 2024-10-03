# Set up and run this Streamlit App
import streamlit as st

st.title("About Us")

st.header("Project Scope")

st.subheader("Objective")
st.write("The objective of this project is to develop, as part of the AI Champions Bootcamp, a web-based LLM-enabled application with use cases that enables citizens to obtain more information regarding the Silver Support Scheme.")

st.subheader("Features")
st.write("The application comprises two main parts:")
st.write("(1) The Silver Support Scheme Policy Explainer provides an interface for users to obtain information regarding the scheme, e.g. benefits, eligibility, payment schedules.")
st.write("(2) The Eligibility Checker allows users to determine whether they qualify for the scheme through input of generic, non-personally identifiable information.")

st.subheader("Data Sources")
st.write("This application uses data from the CPFB Retirement Income page (https://www.cpf.gov.sg/member/retirement-income/government-support/silver-support-scheme) and Silver Support Scheme page (https://www.cpf.gov.sg/member/retirement-income/government-support/silver-support-scheme).")
# project scope, objectives, data sources, and features.