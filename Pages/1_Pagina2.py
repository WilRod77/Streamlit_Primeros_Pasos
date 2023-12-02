import streamlit as st #Noveno paso
import pandas as pd #Noveno paso

st.title("Pagina 02") #Noveno paso

file=st.file_uploader("Sube un archivo con extensión .xlsx",type=["xlsx"]) #Noveno paso

if file is not None: #Noveno paso
   df=pd.read_excel(file) #Noveno paso
   st.write("datos del archivo: "+file.name) #Noveno paso
   st.dataframe(df) #Noveno paso