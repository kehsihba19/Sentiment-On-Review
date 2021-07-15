import streamlit as st
import requests

def app():
    st.title('Thank you')
    with(st.spinner("Calling a happy doggo for you")):
        x=requests.get('https://dog.ceo/api/breed/shiba/images/random').json()
        st.success('Here is a cute doggo to make you happy.')
        st.image(x['message'],use_column_width='always' )