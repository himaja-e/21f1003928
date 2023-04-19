import streamlit as st

def largest_num(a, b, c):
    return max(a, b, c)

st.title("Find the largest of three numbers")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

if st.button("Find the largest"):
    result = largest_num(num1, num2, num3)
    st.success(f"The largest number is {result}")

