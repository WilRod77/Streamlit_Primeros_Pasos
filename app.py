import streamlit as st

st.set_page_config(page_title="Hello", page_icon=":D") #Primer paso
st.title("Hello World") #Primer paso
st.header("This is a header") #Primer paso
st.subheader("This is a subheader")#Primer paso

st.markdown("#This is a markdown")#Primer paso
st.markdown("""##This is a markdown
            This is a markdown
            --- 
            

            -[x] Este es un bullet
            -[x] Este es un bullet
            -[x] Este es un bullet

            * este es una viñeta
            * este es una viñeta

        *Este es un texto en negrita*
            ))
                 


            """)#Primer paso | Se elimina esta parte en la versión de Piña

st.markdown("---")#Tercer paso
            
st.success("Ud Selecciono:")#Segundo Paso

st.success("Exitoso!!")#Segundo Paso
st.info("Info")#Segundo Paso
st.warning("Warning")#Segundo Paso
st.error("Error")#Segundo Paso

st.write("This is a Write") #Segundo Paso

st.markdown("# Elementos dinámicos")#Tercer paso

st.checkbox("Checkbox")#Tercer paso
st.radio("Radio",("Option 1","Option 2"))#Tercer paso
st.button("Button")#Tercer paso
st.selectbox("Selectbox",("Option 1","Option 2"))#Tercer paso
st.multiselect("Multiselect",("Option 1","Option 2"))#Tercer paso
st.slider("Slider",0,100)#Tercer paso
st.select_slider("Select_slider",("Option 1","Option 2"))#Tercer paso
st.text_input("Text_input")#Tercer paso
st.date_input("Date_input")#Tercer paso
st.time_input("Time_input")#Tercer paso

st.markdown("---")#Tercer paso

st.file_uploader("File_uploader")#Tercer paso

st.markdown("---")#Cuarto paso

Entrada_Texto=st.text_input("Text_input2")#Cuarto paso
st.success(Entrada_Texto)

st.markdown("---")#Cuarto paso

Var=st.selectbox("Selectbox2",("Option 1","Option 2"))#Cuarto paso
st.success("Ud selecciono: "+Var)

st.markdown("---")#Quinto paso

st.sidebar.title("Esta es la barra lateral")#Quinto paso
st.sidebar.header("This is a header")#Quinto paso
st.sidebar.radio("Radio2",("Option 1","Option 2"))#Quinto paso
st.sidebar.file_uploader("File_uploader2")#Quinto paso

st.markdown("---")#Sexto paso

col1, col2 = st.columns(2)#Sexto paso
with col1:
    st.write("Column 1")# Sexto paso
    st.write("Column 1.1") # Sexto paso
    st.button("Button2")# Sexto paso
    st.slider("Slider2")# Sexto paso
with col2:
    st.write("Column 2")# Sexto paso

st.markdown("---")#Septimo paso
import pandas as pd #Septimo paso

data={"data":[1,2,3,4]} #Septimo paso
df=pd.DataFrame(data) #Septimo paso
st.dataframe(df) #Septimo paso

st.line_chart(df) #Septimo paso
st.area_chart(df) #Septimo paso
st.bar_chart(df) #Septimo paso

#st.plotly_chart(df) #Septimo paso | Se utiliza para ajustar las condiciones del gráfico

#st.pyplot(fig) #Septimo paso

st.markdown("---")#Octavo paso

import time #Octavo paso
latest_iteration = st.empty() #Octavo paso
bar = st.progress(0) #Octavo paso

for i in range(100): #Octavo paso
    latest_iteration.text(f'Iteration {i+1}')  #Octavo paso
    bar.progress(i + 1)  #Octavo paso
    time.sleep(0.1)  #Octavo paso