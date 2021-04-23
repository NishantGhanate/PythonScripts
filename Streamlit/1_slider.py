import streamlit as st
x = st.slider('x')
st.write(x, 'squared is', x * x)


values = st.slider('Select a range of values',  0, 100, (50))
st.write('Values:', values)


values1 = st.slider('Select a range of values',  0, 100, (25,50))
st.write('Values:', values1)

values2 = st.slider('Select a range of values', (50))
st.write('Values:', values2)


