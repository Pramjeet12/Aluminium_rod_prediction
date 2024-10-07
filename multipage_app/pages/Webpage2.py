import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("aluminium_parameter_model_pickle", "rb") as file:
        data = pickle.load(file)
    return data

data = load_model()




st.title("Aluminium Parameters Prediction")

st.write("""### We need some information to predict the aluminium parameters""")

Elongation = st.number_input("Elongation(in %) ",0.00,2550.00)
Conductivity = st.number_input("Conductivity(in %IACS)",0.00,2500.00)
UTS = st.number_input("UTS(in Mpa)",0.00,2000.00)
ok = st.button("Predict aluminium parameters")
if ok:
    input_data = (Elongation, Conductivity, UTS)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = data.predict(input_data_reshaped)
    prediction_ = [[f"{num:.2f}" for num in row] for row in prediction]
    st.write(f"CastingTemperature(C): {prediction[0][0]:.2f}")
    st.write(f"RollingSpeed(m/min): {prediction[0][1]:.2f}")
    st.write(f"CoolingRate(C/s): {prediction[0][2]:.2f}")
    st.write(f"ChemicalComposition(Al%): {prediction[0][3]:.2f}")
    st.write(f"ChemicalComposition(Cu%): {prediction[0][4]:.2f}")
    st.write(f"ChemicalComposition(Fe%): {prediction[0][5]:.2f}")
    st.write(f"EmulsionTemperature(C): {prediction[0][6]:.2f}")
    st.write(f"EmulsionPressure(Bar): {prediction[0][7]:.2f}")
    st.write(f"EmulsionConcentration(%): {prediction[0][8]:.2f}")
