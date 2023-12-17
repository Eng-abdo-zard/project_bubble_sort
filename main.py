import streamlit as st

from models.bubble_sort import bubble_sort_ascending, bubble_sort_descending

numbers_container, type_container = st.columns([0.8, 0.2])

with numbers_container:
    numbers = st.text_input("Enter numbers:", value="1, 2, 3, 4, 5")

with type_container:
    type = st.selectbox("Type", options=["ascending", "descending"], index=0)

if numbers:
    array = [int(number) for number in numbers.split(",")]

    if type == "ascending":
        bubble_sort_ascending(array)
    else:
        bubble_sort_descending(array)
