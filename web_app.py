import streamlit as st
from phishingdetection import predict_safety

st.title('Website Safety Checker')

url = st.text_input('Enter the URL:')

if st.button('Check Safety'):
    if not url:
        st.warning('Please enter a URL.')
    else:
        try:
            safety_prediction = predict_safety(url)
            if safety_prediction == 1:
                st.success('We guess it is a safe website.')
            else:
                st.error('Caution! Suspicious website detected.')
        except Exception as e:
            st.error(f'An error occurred: {str(e)}')
