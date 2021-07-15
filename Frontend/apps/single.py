import streamlit as st
import requests

def app():
    st.title('Analyse Review')

    single_review = st.text_area('Single Review Analysis')
    
    if st.button("Submit"):
        if(len(single_review)):
            with st.spinner('Analysing the product review'):
                url='https://fastapi-review.herokuapp.com/api/'
                x=requests.post(url,json={'review':single_review}).json()
                if x['Message']=='Positive':
                    st.success("""## Great Work there! People liked your product 😃""")
                else:
                    st.error("""## Try improving your product! People didn't find your product upto the mark 😔""")
        else:
            st.info("Enter the text to be reviewed")
