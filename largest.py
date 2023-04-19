import streamlit as st


st.title("Find the largest of three numbers")

a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")

if st.button("Find the largest"):
    if(a>b and a>c):
        l=a
    elif(b>a and b>c):
        l=b
    elif(c>a and c>b):
        l=c
    else:
        l=a
if st.button("Find the largest"):
    st.success(f"The largest number is {l}")

