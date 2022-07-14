import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px
import streamlit as st
#from bokeh.plotting import figure
#import altair as alt

df = pd.read_csv("penguins_size.csv")
#st.write will help to write data in application and head() will show the head of data.
st.write(df.head())

st.title("Seaborn and Matplotlib Histograms")

# Making Saeborn Chat
st.subheader("Seaborn Chart")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(df['flipper_length_mm'])
plt.xlabel('Flipper_length_mm')
st.pyplot(fig_sb)

# Making Matplotlib chart 
st.subheader('Matploblib Chart')
fig_mp, ax_mpl = plt.subplots()
ax_mp = plt.hist(df['flipper_length_mm'])
plt.xlabel('Flipper_length_mm')
plt.ylabel('Count')
st.pyplot(fig_mp)