import streamlit as st
import pandas as pd
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px

import requests



def app():
    count_positive = 0
    count_negative = 0
    st.title('Analyse Multiple reviews')
    uploaded_file = st.file_uploader("Upload your input CSV file(the first column in the csv must contain the reviews)", type=["csv"])
    
    if uploaded_file is not None:
        with st.spinner('Let the review be fetched and analysed'):
            uploaded_file.seek(0)
            input_df = pd.read_csv(uploaded_file, low_memory=False)
            for i in range(input_df.shape[0]):
                url='https://backend-fastapi.herokuapp.com/api/'
                x=requests.post(url,json={'review':input_df['Review'][i]}).json()
                result = x['Message']
                if result=='Positive':
                    count_positive+=1
                else:
                    count_negative+=1

            x = ["Yes", "No"]
            y = [count_positive, count_negative]

            if count_positive>count_negative:
                st.success("""## Great Work there! Majority of people liked your product 😃""")
            elif count_negative>count_positive:
                st.error("""## Try improving your product! Majority of people didn't find your product upto the mark 😔""")
            else:
                st.info("""## Good Work there, but there's room for improvement! Majority of people have neutral reactions to your product 😶""")


            with st.beta_expander('Visualize'):
                fig = go.Figure()
                layout = go.Layout(
                    title = 'Multiple Reviews Analysis',
                    xaxis = dict(title = 'Category'),
                    yaxis = dict(title = 'Number of reviews'),)
                
                fig.update_layout(dict1 = layout, overwrite = True)
                fig.add_trace(go.Bar(name = 'Multi Reviews', x = x, y = y))
                st.plotly_chart(fig, use_container_width=True)

            with st.beta_expander('Dataset'):
                st.write(input_df)