import streamlit as st

def addition(a,b):
  return(a+b)

a = st.number_input("first number : ")
b = st.number_input("second number : ")

st.text(addition(a,b))
