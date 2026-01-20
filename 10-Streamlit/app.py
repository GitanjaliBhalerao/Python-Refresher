import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello Streamlit")
st.title("This is a title sample")

## Diplay a Simple Text
st.write("This is a simple text")
st.write("Here's our first attempt at using data to create a table:")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write(df)

x = st.slider('x')  # 👈 this is a widget
st.write(f"The slider number you picked is {x}")
st.write(x, 'squared is', x * x)

## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)


##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)