import pickle
import pandas as pd

def demonstrate_location_impact():
    """Demonstrate how location affects house prices"""
    
    print("🏙️ LOCATION IMPACT DEMONSTRATION")
    print("=" * 50)
    
    # Load the enhanced model and encoder
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("city_encoder.pkl", "rb") as f:
            city_encoder = pickle.load(f)
        print("✅ Enhanced model with location support loaded!")
    except FileNotFoundError:
        print("❌ Enhanced model files not found. Please run train_model.py first.")
        return
    
    # Test same house in different cities
    test_house = {"size": 1200, "bedrooms": 3}
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Chennai', 'Hyderabad', 'Kolkata', 'Ahmedabad', 'Jaipur', 'Lucknow']
    
    print(f"\n🏠 SAME HOUSE IN DIFFERENT CITIES:")
    print(f"   House: {test_house['size']} sq ft, {test_house['bedrooms']} BHK")
    print("-" * 50)
    
    results = []
    for city in cities:
        # Encode city
        city_encoded = city_encoder.transform([city])[0]
        
        # Make prediction
        features = pd.DataFrame({
            "sizes": [test_house['size']],
            "bedrooms": [test_house['bedrooms']], 
            "city_encoded": [city_encoded]
        })
        
        prediction = model.predict(features)[0]
        
        # Format price
        if prediction >= 10000000:
            formatted_price = f"₹{prediction/10000000:.2f} Cr"
        elif prediction >= 100000:
            formatted_price = f"₹{prediction/100000:.2f} L"
        else:
            formatted_price = f"₹{prediction:,.0f}"
        
        results.append((city, prediction, formatted_price))
        print(f"📍 {city:10}: {formatted_price}")
    
    # Analysis
    results.sort(key=lambda x: x[1], reverse=True)
    most_expensive = results[0]
    least_expensive = results[-1]
    
    print(f"\n📊 PRICE ANALYSIS:")
    print(f"   Most Expensive: {most_expensive[0]} - {most_expensive[2]}")
    print(f"   Least Expensive: {least_expensive[0]} - {least_expensive[2]}")
    
    price_difference = most_expensive[1] - least_expensive[1]
    price_ratio = most_expensive[1] / least_expensive[1]
    
    print(f"   Price Difference: ₹{price_difference/100000:.2f} L")
    print(f"   Price Ratio: {price_ratio:.1f}x more expensive")
    
    print(f"\n🎯 KEY INSIGHTS:")
    print(f"   ✅ Location parameter dramatically affects prices")
    print(f"   ✅ Same house can vary by {price_ratio:.1f}x based on city")
    print(f"   ✅ Model now considers regional price variations")
    print(f"   ✅ Much more realistic than generic pricing")
    
    # Compare different house sizes in same city
    print(f"\n🏘️ DIFFERENT HOUSE SIZES IN MUMBAI:")
    print("-" * 40)
    
    mumbai_encoded = city_encoder.transform(['Mumbai'])[0]
    house_configs = [
        {"size": 600, "bedrooms": 1, "type": "1BHK"},
        {"size": 900, "bedrooms": 2, "type": "2BHK"},
        {"size": 1200, "bedrooms": 3, "type": "3BHK"},
        {"size": 1800, "bedrooms": 4, "type": "4BHK"}
    ]
    
    for config in house_configs:
        features = pd.DataFrame({
            "sizes": [config['size']],
            "bedrooms": [config['bedrooms']], 
            "city_encoded": [mumbai_encoded]
        })
        
        prediction = model.predict(features)[0]
        
        if prediction >= 10000000:
            formatted_price = f"₹{prediction/10000000:.2f} Cr"
        elif prediction >= 100000:
            formatted_price = f"₹{prediction/100000:.2f} L"
        else:
            formatted_price = f"₹{prediction:,.0f}"
        
        print(f"🏠 {config['type']} ({config['size']} sq ft): {formatted_price}")

if __name__ == "__main__":
    demonstrate_location_impact()
