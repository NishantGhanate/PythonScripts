import streamlit as st
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import cv2


def plotrRgb(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    st.image(img, caption='RGB image',use_column_width=True)
    b,g,r = cv2.split(img) 
    r = r[: , 0]
    g = g[: , 0]
    b = b[: , 0]
    hist_data = [r,g,b]
    group_labels = ['Red', 'Green', 'Blue']
    fig = ff.create_distplot( hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig)

def plotGrey(img):
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    st.image(grey, caption='Gray scale image',use_column_width=True)
    # alternative way to find histogram of an image 
    plt.hist(grey.ravel(),256,[0,256]) 
    st.pyplot()
    # st.write(grey.ravel())


path = st.text_input('File path test on windows', '')
st.write('Filepath = ', path)
img = cv2.imread(path)
if type(img) != type(None):
    plotrRgb(img)
    plotGrey(img)
# img = cv2.imread('G:\Github\PythonScripts\Streamlit\sunrise.jpg')


