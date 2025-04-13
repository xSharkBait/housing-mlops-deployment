import pandas as pd
import gradio as gr
import joblib

# Load the pretrained model.
model = joblib.load('model.pkl')

# Function used to predict price. Takes three inputs and outputs a prediction.
def predict_price(area, bedrooms, bathrooms):
    input_df = pd.DataFrame({"area": [area], "bedrooms": [bedrooms], "bathrooms": [bathrooms]})
    prediction = model.predict(input_df)
    return f"${prediction[0]:,.2f}"

# Instantiate Gradio object with labels and necessary information. Also calls the predict_price function.
iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Area"),
        gr.Number(label="Number of Bedrooms"),
        gr.Number(label="Number of Bathrooms")
    ],
    outputs="text",
    title="House Price Predictor",
    description="Enter area, number of bedrooms, and number of bathrooms to estimate house price."
)

# Launches the Gradio server locally on http://127.0.0.1:7860/
if __name__ == "__main__":
    iface.launch()
