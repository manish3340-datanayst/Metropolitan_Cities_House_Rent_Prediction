from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
import sklearn

# Load model
model = pickle.load(open('lr_model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'bedroom': int(request.form['bedroom']),
        'area': int(request.form['area']),
        'furnish_type': request.form['furnish_type'].lower(),
        'bathroom': int(request.form['bathroom']),
        'property_type': request.form['property_type'].lower(),
        'locality': request.form['locality'].lower(),
        'City': request.form['city']
    }

    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]

    return render_template(
        'index.html', prediction_text=f"Predicted Rent: ₹{int(prediction):,}")


if __name__ == "__main__":
    app.run(debug=True)
