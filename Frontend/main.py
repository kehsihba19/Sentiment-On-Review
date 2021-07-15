import streamlit as st
from multiapp import MultiApp
from apps import home,multiple,single,thanks # import your app modules here

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
app.py
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


app = MultiApp()

st.markdown("""
# Sentiment Analysis for products
This is a multi-page app made using Streamlit which analyses product reviews.
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Check Single Review", single.app)
app.add_app("Check Multiple Review", multiple.app)
app.add_app("Thanks Page", thanks.app)

# The main app
app.run()