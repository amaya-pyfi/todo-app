import streamlit as st
import functions
todos=functions.get_todos()
st.title("My todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)
st.text_input(label="",placeholder="Add a new todo")