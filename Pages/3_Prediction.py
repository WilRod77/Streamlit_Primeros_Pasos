import streamlit as st
import pickle
import pandas as pd

st.title("Predicción de la clase") #Onceavo paso

#with open('Models\RandomForestClassifier.pkl', 'rb') as file: #Onceavo paso
#    modelGB_cargando = pickle.load(file) #Onceavo paso
                        
# print(modelGB_cargando)

@st.cache_resource
def load_model(modelName): #Doceavo paso
    with modelopen(f'Models/Data/model{modelName}.pkl', 'rb') as gb: #Doceavo paso
        model=pickle.load(gb) #Doceavo paso
    return model #Doceavo paso

model_text=st.selectbox("Select a model", options=["Bayesian","Random Forest","ExtraTrees","Gradient Boosting","Decision Tree","Random Forest Classifier","Logistic Regression","XGB Classifier"]) #Doceavo paso

model=None #Doceavo paso
try:
    if model_text=="Bayesian":
        st.write("Bayesian")
        model=load_model("B")
    elif model_text=="Random Forest":
        st.write("Random Forest")
        model=load_model("RF")
    elif model_text=="ExtraTrees":
        st.write("ExtraTrees")
        model=load_model("ET")
    elif model_text=="Gradient Boosting":
        st.write("Gradient Boosting")
        model=load_model("GB")
    elif model_text=="Decision Tree":
        st.write("Decision Tree")
        model=load_model("DT")
    elif model_text=="RandomForestClassifier":
        st.write("RandomForestClassifier")
        model=load_model("RFc")
    elif model_text=="Logistic Regression":
        st.write("Logistic Regression")
        model=load_model("LR")
    elif model_text=="XGB Classifier":
        st.write("XGB Classifier")
        model=load_model("XGBc")

    st.sidebar.success(f"{model_text} Model Loaded") #Doceavo paso
except:
    st.subheader(f"{model_text} Model Not Loaded") #Doceavo paso

st.subheader("Machine Learning Model Selected") #Doceavo paso

st.subheader(model_text,"is a algorithm used as a Machine Learning Model") #Doceavo paso
st.write("Define of the algorithm implemented for predict the flow patterns") #Doceavo paso

features=["Current_Medicines","Age","Sex","BP","Cholesterol","Na_to_K"] #Treceavo paso
st.write("to continue, select the features") #Treceavo paso

def user_input_parameters(): #Treceavo paso
    inputs={} #
    for i, feature in enumerate(features):
        row, col=i//3,i%3
        with st.container():
            if i % 3 == 0:
                cols=st.columns(3)
            # inputs[feature]=cols[col].text_input(feature) #Treceavo paso
            inputs[feature]=cols[col].number_input(feature) #Treceavo paso
            
    data_features={
        'Vsl':inputs[features[0]],
        'Age':inputs[features[1]],
        'Sex':inputs[features[2]],
        'BP':inputs[features[3]],
        'Cholesterol':inputs[features[4]],
        'Na_to_K':inputs[features[5]]
        }   

    features_df=pd.DataFrame(data_features, index=[0]) #Treceavo paso
    return features_df #Treceavo paso

df=user_input_parameters() #Treceavo paso

#Create a new DataFrame with a row aditional 'Value'
df=df.T.reset_index() #Catorceavo paso
df.columns=["Feature","Value"] #Catorceavo paso
df=df.set_index("Feature").T #Catorceavo paso

st.table(df) #Catorceavo paso

st.subheader("Prediction of the pattern of Current Medicines") #Catorceavo paso

predict_button, clear_button=st.columns(2) #Catorceavo paso

predict_clicked=predict_button.button("Predict") #Catorceavo paso
clear_clicked=clear_button.button("Clear") #Catorceavo paso

prediction=None #Catorceavo paso

if predict_clicked:
    #It's necesary to define that all values as numeric value
    for value in df.values.flatten():
        # if not value or not value.isdigit():
        if not value:
            st.warning("All values must be numeric")
            break
        else:
            prediction=model.predict(df) #Catorceavo paso

    st.success(f"The pattern of Current Medicines is: {prediction[0]}") #Catorceavo paso
    
    #Define a dictionary for asociate the prediction with the descriptions
    prediction_descriptions={
        'DB': 'Flujo de burbujas dispersas (DB)',
        'SS': 'Flujo estratificado uniforme (SS)',
        'SW': 'Flujo estratificado ondulado (SW)',
        'A': 'Flujo anular (A)',
        'I': 'Flujo intermitente (I)',
        'B': 'Flujo de burbujas (B)'
    }

    #Show the complete description of the predictions
    st.sucess(prediction_descriptions[prediction[0]]) #Catorceavo paso

    if prediction[0] in ["I","A"]:
        st.warning("The prediction is not reliable") #Catorceavo paso
