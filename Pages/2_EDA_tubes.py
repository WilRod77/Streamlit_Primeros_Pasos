import streamlit as st #Decimo paso
import pandas as pd #Decimo paso
import matplotlib.pyplot as plt #Decimo paso

def plot_histogram(Column): #Decimo paso
   plt.figure(figsize=(6,4)) #Decimo paso
   plt.hist(data[Column], bins=20, color="purple", edgecolor="black") #Decimo paso
   plt.title(title) #Decimo paso
   plt.xlabel(Column) #Decimo paso
   plt.ylabel("Frecuency") #Decimo paso
   return plt #Decimo paso

def box_plot(Column): #Decimo paso
   plt.figure(figsize=(6,4)) #Decimo paso
   plt.boxplot(data[Column]) #Decimo paso
   plt.title(title) #Decimo paso
   plt.xlabel(Column) #Decimo paso
   plt.ylabel("Values") #Decimo paso
   return plt #Decimo paso

st.title("EDA") #Decimo paso

data=pd.read_csv("Models\Data\Current_Medicines.csv") #Decimo paso

#name_clases={0:"DB", 1:"SS",2:"SW",3:"A",4:"I",5:"B"} #Decimo paso
#data["Current_Medicines"]=data["Current_Medicines"].replace(name_clases) #Decimo paso

st.dataframe(data) #Decimo paso

st.subheader("Descriptive statistics of current medicines") #Decimo paso
st.dataframe(data.describe()) #Decimo paso

st.markdown("---") #Decimo paso

col1, col2=st.columns(2) #Decimo paso

with col1: #Decimo paso
   title="Histogram of Current_Medicines" #Decimo paso
   selected_Column=st.selectbox("Select Column",data.columns) #Decimo paso
   #st.pyplot(plot_histogram(selected_Column, f"Histogram of {selected_Column}")) #Decimo paso

with col2: #Decimo paso
   title="Boxplot of Current_Medicines" #Decimo paso
   selected_Column=st.selectbox("Select other Column",data.columns) #Decimo paso
   #st.pyplot(box_plot(selected_Column, f"Boxplot of {selected_Column}")) #Decimo paso

st.markdown("---") #Decimo paso
   