import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("aluminium_model_pickle", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()




st.title("Aluminium Properties Prediction")

st.write("""### We need some information to predict the aluminium properties""")

CastingTemperature = st.number_input("CastingTemperature(in C) ",0.00,2550.00)
RollingSpeed = st.number_input("RollingSpeed(in m/min)",0.00,500.00)
CoolingRate = st.number_input("CoolingRate(in C/s)",0.00,200.00)
ChemicalCompositionAl = st.number_input("ChemicalCompositionAl(in %)",0.00,200.00)
ChemicalCompositionCu = st.number_input("ChemicalCompositionCu(in %)",0.00,200.00)
ChemicalCompositionFe = st.number_input("ChemicalCompositionFe(in %)",0.00,200.00)
EmulsionTemperature = st.number_input("EmulsionTemperature(in C)",0.00,200.00)
EmulsionPressure = st.number_input("EmulsionPressure(in Bar)",0.00,200.00)
EmulsionConcentration = st.number_input("EmulsionConcentration(in %)",0.00,200.00)
ok = st.button("Predict aluminium properties")
if ok:
    input_data = (CastingTemperature,RollingSpeed,CoolingRate,ChemicalCompositionAl,ChemicalCompositionCu,ChemicalCompositionFe,EmulsionTemperature,EmulsionPressure,EmulsionConcentration)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = data.predict(input_data_reshaped)
    st.write(f"Elongation (%): {prediction[0][0]:.2f}")
    st.write(f"Conductivity (%IACS): {prediction[0][1]:.2f}")
    st.write(f"UTS (MPa): {prediction[0][2]:.2f}")