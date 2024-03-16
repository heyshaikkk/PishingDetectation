import streamlit as st
import numpy as np
import phishingdetection

def predict_safety(url):
    x = np.array(obj.getFeaturesList(url)).reshape(1, 30)
    y_pred = gbc.predict(x)[0]
    return y_pred


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