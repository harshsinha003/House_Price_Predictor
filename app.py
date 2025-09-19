"""
House Price Predictor - Flask API Server
Enhanced Indian Housing Model with Location-based Pricing
"""
import pickle
import pandas as pd
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)


@app.route("/api/predict/", methods=["POST"])
def index():
    data = request.json
    sizes = data["sizes"]
    bedrooms = data["bedrooms"]
    cities = data.get("cities", ["Delhi"] * len(sizes))  # Default to Delhi if not provided

    # Load model and city encoder
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    try:
        with open("city_encoder.pkl", "rb") as f:
            city_encoder = pickle.load(f)

        # Encode cities
        city_encoded = city_encoder.transform(cities)

        new_data = pd.DataFrame({
            "sizes": sizes,
            "bedrooms": bedrooms,
            "city_encoded": city_encoded
        })
    except FileNotFoundError:
        # Fallback to old model without city encoding
        new_data = pd.DataFrame({"sizes": sizes, "bedrooms": bedrooms})

    prices = model.predict(new_data).tolist()
    results = []

    for i, (size, bedroom, price) in enumerate(zip(sizes, bedrooms, prices)):
        # Format price in Indian Rupees with proper formatting
        if price >= 10000000:  # 1 Crore or more
            formatted_price = f"₹{price/10000000:.2f} Cr"
        elif price >= 100000:  # 1 Lakh or more
            formatted_price = f"₹{price/100000:.2f} L"
        else:
            formatted_price = f"₹{price:,.0f}"

        result = {
            "size": size,
            "bedroom": bedroom,
            "predicted_price": formatted_price,
            "predicted_price_raw": int(price)  # Raw value for calculations
        }

        # Add city if available
        if i < len(cities):
            result["city"] = cities[i]

        results.append(result)

    return jsonify({"message": "Prediction results", "results": results})
