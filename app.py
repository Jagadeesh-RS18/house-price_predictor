from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

# Initialize Flask app
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from form
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    location = request.form['Location']

    # Create input DataFrame
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, location]],
                              columns=['Area', 'Bedrooms', 'Bathrooms', 'Location'])

    # Make prediction
    prediction = model.predict(input_data)[0]
    price = round(prediction, 2)

    # Render result page
    return render_template('result.html', price=f"₹{price:,.2f}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
