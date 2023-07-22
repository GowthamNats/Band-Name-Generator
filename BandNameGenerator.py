import streamlit as st

st.title("Band Name Generator")

city_name = st.text_input("Enter the name of your city: ")
pet_name = st.text_input("Enter the name of your pet: ")

if st.button("Generate"):
    st.header(f"Band Name: {city_name} {pet_name}")