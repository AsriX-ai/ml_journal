import streamlit as st
import pandas as pd

#title widget
st.title("Streamlit Text Input")

#text_input widget
name = st.text_input("Enter your name:")
if name:
    st.write(f"Thank you for using this widget {name}")
    
#slider widget
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}")

#selectbox widget
prgm_choice = ["Python", "C", "C++", "Java", "JavaScript"]
usr_choice = st.selectbox("Choose your language:", prgm_choice)
st.write(f"You selected {usr_choice}")

#dataframe
data = {
    "Name": ["Rosy", "Mary", "Angel", "Victor"],
    "Age" : [28, 24, 25, 27],
    "City" :["New York", "India", "Chicago", "Belgium"]
}

df = pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

