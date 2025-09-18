"""
House Price Predictor - Enhanced Model with Location
ML model training with city-specific pricing for Indian real estate
"""
# Enhanced Model with Location Parameter
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def generate_enhanced_indian_housing_data(n_samples=1000):
    """Generate realistic Indian housing data with location parameter"""
    np.random.seed(42)
    
    # Define Indian cities with their typical price ranges
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Chennai', 'Hyderabad', 'Kolkata', 'Ahmedabad']
    city_price_multipliers = {
        'Mumbai': 3.5,      # Most expensive
        'Delhi': 2.8,
        'Bangalore': 2.2,
        'Pune': 1.8,
        'Chennai': 1.6,
        'Hyderabad': 1.5,
        'Kolkata': 1.3,
        'Ahmedabad': 1.2    # Most affordable
    }
    
    # Generate data
    data = []
    for i in range(n_samples):
        # Random city selection
        city = np.random.choice(cities)
        multiplier = city_price_multipliers[city]
        
        # Generate house size (500-3000 sq ft)
        size = np.random.normal(1200, 400)
        size = np.clip(size, 500, 3000)
        
        # Generate bedrooms based on size
        bedrooms = np.round(size / 400 + np.random.normal(0, 0.5))
        bedrooms = np.clip(bedrooms, 1, 5).astype(int)
        
        # Base price per sq ft (adjusted by city)
        base_price_per_sqft = np.random.normal(4000, 800) * multiplier
        base_price_per_sqft = np.clip(base_price_per_sqft, 2000, 25000)
        
        # Calculate price
        bedroom_premium = bedrooms * np.random.normal(150000, 30000) * multiplier
        base_price = size * base_price_per_sqft + bedroom_premium
        
        # Add noise
        noise = np.random.normal(0, 200000)
        final_price = base_price + noise
        final_price = np.clip(final_price, 1000000, 50000000)
        
        data.append({
            'sizes': int(size),
            'bedrooms': int(bedrooms),
            'city': city,
            'prices': int(final_price)
        })
    
    return pd.DataFrame(data)


def train_enhanced_model():
    """Train model with location parameter"""
    print("🇮🇳 Training Enhanced Indian Housing Model with Location...")
    print("=" * 60)
    
    # Generate enhanced dataset
    df = generate_enhanced_indian_housing_data(1000)
    print(f"✅ Generated {len(df)} samples with location data")
    print(f"📍 Cities included: {df['city'].unique()}")
    
    # Encode city names to numbers
    label_encoder = LabelEncoder()
    df['city_encoded'] = label_encoder.fit_transform(df['city'])
    
    # Features now include: size, bedrooms, city
    X = df[["sizes", "bedrooms", "city_encoded"]]
    y = df["prices"]
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_test_pred = model.predict(X_test)
    test_r2 = r2_score(y_test, y_test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    
    print(f"\n🎯 Enhanced Model Performance:")
    print(f"   R² Score: {test_r2:.4f}")
    print(f"   RMSE: ₹{test_rmse:,.2f}")
    
    # Save both model and encoder
    with open("enhanced_model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    with open("city_encoder.pkl", "wb") as f:
        pickle.dump(label_encoder, f)
    
    print("💾 Enhanced model saved!")
    
    # Test predictions for different cities
    print(f"\n🏙️ SAME HOUSE, DIFFERENT CITIES:")
    print("-" * 40)
    
    test_size, test_bedrooms = 1200, 3
    for city in ['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Ahmedabad']:
        city_encoded = label_encoder.transform([city])[0]
        features = pd.DataFrame({
            "sizes": [test_size],
            "bedrooms": [test_bedrooms], 
            "city_encoded": [city_encoded]
        })
        
        prediction = model.predict(features)[0]
        if prediction >= 10000000:
            formatted_price = f"₹{prediction/10000000:.2f} Cr"
        else:
            formatted_price = f"₹{prediction/100000:.2f} L"
            
        print(f"📍 {city:10}: {formatted_price}")
    
    return model, label_encoder


if __name__ == "__main__":
    train_enhanced_model()
