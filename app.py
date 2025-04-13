import pandas as pd
import gradio as gr
import joblib
from sklearn.model_selection import train_test_split

model = joblib.load('model.pkl')

def predict_price(area, bedrooms, bathrooms):
    input_df = pd.DataFrame({"area": [area], "bedrooms": [bedrooms], "bathrooms": [bathrooms]})
    prediction = model.predict(input_df)
    return f"${prediction[0]:,.2f}"

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

if __name__ == "__main__":
    iface.launch()