import langchain_helper as lch
import streamlit as st

st.title("Chonky a foody recommendation generator")

user_city = st.sidebar.text_area("Please enter your city name", max_chars=20)
food_allergy = st.sidebar.text_area("What is your food allergy?", max_chars=15)

if user_city:
    response = lch.city_foods(user_city, food_allergy)
    st.text(response["city_name"])