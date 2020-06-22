import streamlit as st
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import random

URI = 'http://127.0.0.1:5000'

st.title('Neural-Network-Visualizer')
st.sidebar.markdown('## Input Image')

if st.button('Get prediction'):
    response = requests.post(URI,data={})
    response = json.load(response)
    preds = response.get('prediction')
    image = response.get('image')
    image = np.reshape(image, (28,28))
    
    st.sidebar.image(image, width=150)
    
    for layer , p in enumerate(preds):
        
        numbers = np.squeez(np.array(p))
        
        plt.figure(figsize=(32,4))
        
        if layer==2:
            row=1
            col=10
        else:
            row=2
            col=16
            
        for l, number in enumerate(numbers):
            plt.subplot(row,col,i+1)
            plt.imshow(number * np.ones(8,8,3).astype('float32'))
            plt.xticks([])
            plt.yticks([])
            
            if layer ==2:
                plt.xlabel(str(i), fontsize=40)
        plt.subplots_adjust(wspace=0.05, hspace=0.05)
        plt.tight_layout()
        st.pyplot()
        
    
