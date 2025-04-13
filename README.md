# House Price Predictor

## Overview
This repository provides a simple house price prediction application. Built with Python, this app uses a pre-trained machine learning model to estimate house prices based on three inputs: area, number of bedrooms, and number of bathrooms. The prediction model is encapsulated in the `model.pkl` file, and the user interface is implemented using the Gradio library. The application serves as an easy-to-use tool for quickly estimating house prices based on the given features.

## Repository Contents
- **app.py**: The main Python script that initializes and launches the Gradio interface for interacting with the prediction model. 
- **model.pkl**: A pre-trained machine learning model saved in pickle format. This model is used by `app.py` to compute the house price predictions.
- **Housing.csv**: The dataset file that was used during the model training and testing process.

## Prerequisites
- Python 3.x installed on your machine.
- The following Python packages:
  - pandas
  - gradio
  - joblib
  - scikit-learn

You can install these packages via pip. If you prefer a virtual environment (recommended), follow the steps below.

## Installation and Setup

### 1. Download the Repository
Open your web browser and enter this link into the address bar to download the repository:
```bash
https://github.com/xSharkBait/housing-mlops-deployment/archive/refs/heads/main.zip
```

### 2. Unzip the Repository
Go to the location of the newly downloaded folder in the file explorer, move it to the desired location, right-click the folder, and select "Extract All..." 

### 2. Navigate to the Repository Directory
Next, open your command prompt (or your preferred IDE) and navigate to the repository directory.

### 3. Install Required Dependencies
In your command prompt, run this command to install the required Dependencies.
```bash
pip install pandas gradio joblib scikit-learn
```

## Running the Application
To launch the house price prediction app, run the following command in your terminal or command prompt:
```bash
python app.py
```

This command will start the Gradio interface. You should now open a new tab in your web browser and navigate to http://127.0.0.1:7860

## **Using the Application**
Once the Gradio interface loads:
- **Input Fields:**
    - **Area:** Enter the house's area (e.g., in square feet).
    - **Number of Bedrooms:** Specify how many bedrooms the house has.
    - **Number of Bathrooms:** Specify how many bathrooms the house has.
- **Prediction:** After filling in the inputs, click the orange submit button. The application will use the pre-trained model to generate an estimated house price and display it directly on the web interface.
