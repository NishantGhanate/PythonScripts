import streamlit as st

# Adds a checkbox to the sidebar
add_selectbox = st.sidebar.checkbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone')))

# Adds a slider to the sidebar
add_slider = st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))