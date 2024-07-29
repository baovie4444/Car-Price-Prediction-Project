from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load the trained model
model = joblib.load('XGBoost_model.pkl')

# This would ideally be a database, but we'll use a list for simplicity
past_predictions = []

@app.route('/')
def home():
    return render_template('index.html', past_predictions=past_predictions)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        form_data = {
            'name': int(request.form['name']),
            'location': int(request.form['location']),
            'year': int(request.form['year']),
            'kilometers_driven': int(request.form['kilometers_driven']),
            'fuel_type': int(request.form['fuel_type']),
            'transmission': int(request.form['transmission']),
            'owner_type': int(request.form['owner_type']),
            'mileage': float(request.form['mileage']),
            'engine': int(request.form['engine']),
            'power': float(request.form['power']),
            'seats': int(request.form['seats'])
        }

        # Prepare feature array for prediction
        features = np.array([[
            form_data['name'], form_data['location'], form_data['year'],
            form_data['kilometers_driven'], form_data['fuel_type'],
            form_data['transmission'], form_data['owner_type'],
            form_data['mileage'], form_data['engine'],
            form_data['power'], form_data['seats']
        ]])

        # Ensure feature names match the training data
        feature_columns = [
            'Name', 'Location', 'Year', 'Kilometers_Driven', 'Fuel_Type',
            'Transmission', 'Owner_Type', 'Mileage', 'Engine', 'Power', 'Seats'
        ]
        features_df = pd.DataFrame(features, columns=feature_columns)

        # Make prediction
        prediction = model.predict(features_df)[0]

        # Save the prediction
        past_predictions.append({
            'car_name': get_car_name(form_data['name']),
            'year': form_data['year'],
            'price': round(prediction, 2),
            'prediction_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # Keep only the last 5 predictions
        if len(past_predictions) > 7:
            past_predictions.pop(0)

        # Render prediction result within the same template
        return render_template('index.html', prediction=prediction, form_data=form_data, past_predictions=past_predictions)

def get_car_name(name_index):
    car_names = [
        "Ambassador", "Audi", "BMW", "Bentley", "Chevrolet",
        "Datsun", "Fiat", "Force", "Ford", "Honda",
        "Hyundai", "Isuzu", "Jaguar", "Jeep", "Lamborghini",
        "Land Rover", "Mahindra", "Maruti", "Mercedes-Benz", "Mini",
        "Mitsubishi", "Nissan", "Porsche", "Renault", "Skoda",
        "Smart", "Tata", "Toyota", "Volkswagen", "Volvo"
    ]
    return car_names[name_index]

if __name__ == '__main__':
    app.run(debug=True)

