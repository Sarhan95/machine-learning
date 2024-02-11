import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from  sklearn.model_selection import train_test_split
import seaborn as sns

st.title("application de machine learning pour detecter une maladie cardiaque")
st.subheader("auteur: zakaria sarhan")
st.markdown("***prédiction  une maladie cardiaque avec apprentissage automoatique***")

@st.cache_data(persist=True)
def load_df():
    data=pd.read_csv("heart.csv")
    return data
df=load_df()
print(df)
st.write(df)
###### affichage des graphique avec plotly
var_qulitative=df.select_dtypes("object").columns.to_list()
var_qunti=df.select_dtypes(exclude="object").columns.to_list()

var_qual=st.selectbox("choisir la variable pour colorer les point",var_qulitative)
var_x=st.selectbox("Choisir la variable en abscisse", var_qunti)
var_y=st.selectbox("Choisir la variable en ordonnée", var_qunti)

fig=px.scatter(data_frame=df,x=var_x,y=var_y,color=var_qual)
st.plotly_chart(fig)
##### utilisation seaborn
fig1,ax1=plt.subplots()
ax1=sns.histplot(df["Age"],kde=True)
plt.xlabel("variation age")
st.pyplot(fig1)
fig2, ax2=plt.subplots()
ax2= plt.hist(df["Age"])
plt.xlabel("variation age")
st.pyplot(fig2)




