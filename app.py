import gradio as gr
import joblib
import numpy as np

# Load your trained model
xgb_clf = joblib.load("xgboost-model.pkl")

# Function for prediction
def predict_death_event(age, anaemia, high_blood_pressure, creatinine_phosphokinase, diabetes, ejection_fraction, platelets, sex, serum_creatinine, serum_sodium, smoking, time):
    # Create a NumPy array with the input features
    input_data = np.array([age, anaemia, high_blood_pressure, creatinine_phosphokinase, diabetes, ejection_fraction, platelets, sex, serum_creatinine, serum_sodium, smoking, time])

    # Reshape the array to a 2D array with a single row
    input_data = input_data.reshape(1, -1)

    # Make the prediction
    prediction = xgb_clf.predict(input_data)[0]

    # Return the prediction
    return "Patient will survive" if prediction == 0 else "Patient will not survive"


# Inputs from user
inputs = [
    gr.Slider(minimum=40, maximum=95, step=1, value=60, label="Age"),
    gr.Radio(choices=[0, 1], value=0, label="Anaemia"),
    gr.Radio(choices=[0, 1], value=0, label="High Blood Pressure"),
    gr.Slider(minimum=23, maximum=7861, step=1, value=582, label="Creatinine Phosphokinase"),
    gr.Radio(choices=[0, 1], value=0, label="Diabetes"),
    gr.Slider(minimum=14, maximum=80, step=1, value=38, label="Ejection Fraction"),
    gr.Slider(minimum=25100, maximum=850000, step=1, value=265000, label="Platelets"),
    gr.Radio(choices=[0, 1], value=0, label="Sex"),
    gr.Slider(minimum=0.5, maximum=9.4, step=0.1, value=1.1, label="Serum Creatinine"),
    gr.Slider(minimum=113, maximum=148, step=1, value=136, label="Serum Sodium"),
    gr.Radio(choices=[0, 1], value=0, label="Smoking"),
    gr.Slider(minimum=4, maximum=285, step=1, value=115, label="Time"),
]

# Output response
outputs = gr.Textbox(label="Prediction")

# Gradio interface to generate UI link
title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

iface = gr.Interface(
    fn=predict_death_event,
    inputs=inputs,  # Using the inputs defined earlier
    outputs=outputs,
    title=title,
    description=description,
    allow_flagging='never'
)

iface.launch(share=True)