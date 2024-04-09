import streamlit as st
from predict import show_predict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()



# def show_page():
#     with open("index.html", "r") as file:
#         html_content = file.read()

#     with open("style.css", "r") as file:
#         css_styles = file.read()

#     st.markdown(html_content, unsafe_allow_html=True)
#     st.markdown(f"<style>{css_styles}</style>", unsafe_allow_html=True)

# show_page()
