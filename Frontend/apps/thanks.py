import streamlit as st
import requests

def app():
    st.title('Thank you')

    st.success('Here is a cute doggo to make you happy.')

    x=requests.get('https://dog.ceo/api/breed/shiba/images/random').json()
    st.image(x['message'],use_column_width='always' )