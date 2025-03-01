import streamlit as st
import pickle 
import numpy as np

with open("model.pkl","rb") as p:
    model=pickle.load(p)
    
with open("mapping.pkl","rb") as f:
    mapping=pickle.load(f)    
    
st.title("Car Price Prediction Application")

st.write("Please enter your advertisement invest in each to predict sales")

MODEL =st.selectbox(" MODEL:",list(set(mapping.keys())))
car_model = mapping[MODEL]  
AGE_08_04 = st.number_input("How old is your car?", min_value=0)
KM = st.number_input("Enter mileage (KM driven)", min_value=0.0, format="%.2f")
HP = st.number_input("Horsepower of your car", min_value=0.0, format="%.2f")
DOORS = st.number_input("Number of doors", min_value=0, max_value=5)
CYLINDERS = st.number_input("Number of cylinders", min_value=0, max_value=12)
GEARS = st.number_input("Number of gears", min_value=0, max_value=8)
WEIGHT = st.number_input("Enter car weight", min_value=0.0, format="%.2f")

   
if st.button("Predict Price"):
    features=np.array([[car_model,AGE_08_04,KM,HP,DOORS,CYLINDERS,GEARS,WEIGHT]])
    predictions=model.predict(features)[0]
    st.success(f"predicted Price:{predictions:.2f}")
  
