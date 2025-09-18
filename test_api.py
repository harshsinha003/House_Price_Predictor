"""
House Price Predictor - API Testing Script
Tests the Flask API endpoints for ML-based price prediction
"""
import requests
import json

def test_api():
    url = "http://localhost:5000/api/predict/"
    
    # Test with typical Indian house configurations including cities
    test_cases = [
        {"sizes": [600], "bedrooms": [1], "cities": ["Mumbai"], "description": "1BHK in Mumbai"},
        {"sizes": [900], "bedrooms": [2], "cities": ["Delhi"], "description": "2BHK in Delhi"},
        {"sizes": [1200], "bedrooms": [3], "cities": ["Bangalore"], "description": "3BHK in Bangalore"},
        {"sizes": [1200], "bedrooms": [3], "cities": ["Ahmedabad"], "description": "3BHK in Ahmedabad"},
        {"sizes": [1500], "bedrooms": [4], "cities": ["Pune"], "description": "4BHK in Pune"}
    ]
    
    print("🇮🇳 Testing Enhanced Indian House Price Prediction API (with Location)")
    print("=" * 70)
    
    for test_case in test_cases:
        try:
            response = requests.post(url, json=test_case)
            print(f"\n🏠 {test_case['description']}:")
            print(f"   Size: {test_case['sizes'][0]} sq ft, {test_case['bedrooms'][0]} bedrooms")
            print(f"   Location: {test_case['cities'][0]}")
            print(f"   Status Code: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                predicted_price = result['results'][0]['predicted_price']
                print(f"   Predicted Price: {predicted_price}")
                print("   ✅ Enhanced API working correctly!")
            else:
                print(f"   ❌ API Error: {response.text}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print(f"\n💡 Location makes a HUGE difference in pricing!")
    print(f"💡 Make sure Flask server is running: python app.py")

if __name__ == "__main__":
    test_api()
