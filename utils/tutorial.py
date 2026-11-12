import streamlit as st

st.title("Title APP")
st.write("Hello from titanic-app!")
radio_value =st.radio("Select a number", [1,2,3], index=1)
checked = st.checkbox("Check me out")

if checked:
    st.write("You checked me")

st.write(radio_value)

with st.form("search"):
    name = st.text_input("Name contains", placeholder="e.g Allen")
    classes = st.multiselect("Class", [1,2,3], default=[2,3])
    ages = st.slider("Age", 0, 1000, (0,100))
    submitted = st.form_submit_button("Search")

if submitted:
    st.write(f"You searched for {name} in classes \
             and ages {ages}")