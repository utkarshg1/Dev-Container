import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='EMI Calculator')
st.title('EMI Calculator - Utkarsh Gaikwad')

P = st.number_input('Please Enter amount in INR : ', min_value=0.00, step=0.01)
N = st.number_input('Please Enter period in years : ', min_value=0.0, step=0.1)
R = st.slider('Please enter Rate of Intrest in %p.a. : ', min_value=0.00, max_value=100.00, step=0.01, value=8.5)

submit = st.button('Calculate EMI')

st.subheader('Results are : ')

def calculate_emi(P, N, R):
    # Convert N to months 
    n = N*12
    r = R/(12*100)
    # Calculate emi
    x = (1+r)**n 
    emi = P*r*x/(x-1)
    amt = n*emi
    return emi, amt 

if submit:
    emi, amt = calculate_emi(P, N, R)
    I = amt - P

    st.subheader(f'EMI : {emi:.2f} INR')
    st.subheader(f'Total Amount : {amt:.2f} INR')
    st.subheader(f'Intrest Paid : {I:.2f} INR')    

    dct = {'Amount':['Intrest', 'Principal'],
        'Value':[I, P]}

    df = pd.DataFrame(dct)

    fig = px.pie(data_frame=df, 
                 names='Amount', 
                 values='Value',
                 color_discrete_sequence=px.colors.qualitative.Plotly)

    st.plotly_chart(fig)
