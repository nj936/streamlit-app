import streamlit as st

st.write(""" # Numerical Addition
Add any two numbers using this app. """)

st.header("Input numbers for addition")

first_number = st.number_input("FIRST NUMBER")
second_number = st.number_input("SECOND NUMBER")
output_number = first_number + second_number

st.subheader("Output")
st.write("Total is: " + str(output_number))
