import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Prediction App")

a = st.number_input("Enter value 1")
b = st.number_input("Enter value 2")
c = st.number_input("Enter value 3")
d = st.number_input("Enter value 4")

if st.button("Predict"):

    data = np.array([[a, b, c, d]])

    prediction = model.predict(data)

    st.write(prediction)
