"""
House Price Predictor - Model Training Script
Machine Learning model for Indian real estate price prediction
Supports 38+ cities with location-based pricing
"""
# train_model.py
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def generate_realistic_indian_housing_data(n_samples=1000):
    """Generate realistic Indian housing data with location parameter"""
    np.random.seed(42)  # For reproducible results
    
    # Define comprehensive Indian cities with their typical price multipliers
    cities = [
        # Tier-1 Metropolitan Cities (Most Expensive)
        'Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Chennai', 'Hyderabad', 'Kolkata',
        
        # Tier-1 Major Cities
        'Ahmedabad', 'Surat', 'Noida', 'Gurgaon', 'Ghaziabad', 'Faridabad',
        
        # Tier-2 State Capitals & Major Cities
        'Jaipur', 'Lucknow', 'Indore', 'Bhopal', 'Kochi', 'Coimbatore', 'Nagpur',
        'Visakhapatnam', 'Thiruvananthapuram', 'Bhubaneswar', 'Chandigarh',
        
        # Tier-2 Industrial & Tech Hubs
        'Mysore', 'Nashik', 'Vadodara', 'Rajkot', 'Kanpur', 'Ludhiana', 'Agra',
        
        # Tier-3 Emerging Cities
        'Guwahati', 'Patna', 'Raipur', 'Dehradun', 'Jammu', 'Amritsar', 'Jalandhar'
    ]
    
    city_price_multipliers = {
        # Tier-1 Metropolitan (₹15,000-25,000 per sq ft)
        'Mumbai': 4.5,      # Most expensive - SoBo, Bandra
        'Delhi': 3.8,       # NCR - Central Delhi, CP area  
        'Gurgaon': 3.5,     # IT hub, corporate offices
        'Noida': 3.2,       # IT sector, close to Delhi
        'Bangalore': 3.0,   # IT capital of India
        'Pune': 2.8,        # IT hub, automobile sector
        'Chennai': 2.5,     # IT corridor, automobile hub
        'Hyderabad': 2.3,   # HITEC City, pharma hub
        'Kolkata': 2.0,     # Cultural capital
        
        # Tier-1 Major Cities (₹8,000-15,000 per sq ft)
        'Ahmedabad': 1.8,   # Commercial capital of Gujarat
        'Surat': 1.6,       # Diamond & textile hub
        'Ghaziabad': 1.8,   # Delhi NCR extension
        'Faridabad': 1.7,   # Industrial hub near Delhi
        
        # Tier-2 State Capitals (₹6,000-10,000 per sq ft)
        'Jaipur': 1.5,     # Pink city, tourism
        'Lucknow': 1.3,    # UP capital
        'Bhopal': 1.2,     # MP capital
        'Indore': 1.4,     # Commercial hub MP
        'Chandigarh': 2.2,  # Planned city, Punjab/Haryana capital
        'Kochi': 1.6,      # IT hub Kerala
        'Thiruvananthapuram': 1.4,  # Kerala capital
        'Coimbatore': 1.3,  # Textile hub Tamil Nadu
        'Nagpur': 1.2,     # Orange city, central India
        'Visakhapatnam': 1.3, # Port city Andhra Pradesh
        'Bhubaneswar': 1.3, # Odisha capital, IT growth
        
        # Tier-2 Industrial Hubs (₹5,000-8,000 per sq ft)
        'Vadodara': 1.3,   # Petrochemical hub Gujarat
        'Rajkot': 1.2,     # Industrial city Gujarat
        'Nashik': 1.3,     # Wine capital, near Mumbai
        'Mysore': 1.2,     # IT city near Bangalore
        'Kanpur': 1.1,     # Industrial city UP
        'Ludhiana': 1.2,   # Industrial hub Punjab
        'Agra': 1.0,       # Heritage city UP
        
        # Tier-3 Emerging Cities (₹3,000-6,000 per sq ft)
        'Patna': 1.0,      # Bihar capital
        'Guwahati': 1.1,   # Gateway to Northeast
        'Raipur': 0.9,     # Chhattisgarh capital
        'Dehradun': 1.2,   # Uttarakhand capital, hill station
        'Jammu': 1.0,      # J&K winter capital
        'Amritsar': 1.1,   # Golden temple city
        'Jalandhar': 1.0   # Sports goods hub Punjab
    }
    
    data = []
    for i in range(n_samples):
        # Random city selection
        city = np.random.choice(cities)
        multiplier = city_price_multipliers[city]
        
        # Generate realistic house sizes (500 to 3000 sq ft - typical for India)
        size = np.random.normal(1200, 400)
        size = np.clip(size, 500, 3000)
        
        # Generate bedrooms based on size (realistic correlation for Indian homes)
        bedrooms = np.round(size / 400 + np.random.normal(0, 0.5))
        bedrooms = np.clip(bedrooms, 1, 5).astype(int)
        
        # Generate prices with realistic Indian market relationships (location-adjusted)
        # Base price per sq ft varies from ₹3,000-₹8,000 but adjusted by city multiplier
        base_price_per_sqft = np.random.normal(4000, 800) * multiplier
        base_price_per_sqft = np.clip(base_price_per_sqft, 2000, 20000)
        
        # Bedroom premium (each bedroom adds value in Indian context, location-adjusted)
        bedroom_premium = bedrooms * np.random.normal(150000, 30000) * multiplier
        
        # Calculate base prices
        base_price = size * base_price_per_sqft + bedroom_premium
        
        # Add some realistic noise
        noise = np.random.normal(0, 200000)
        final_price = base_price + noise
        
        # Ensure prices are reasonable for Indian market (varies by city)
        min_price = 1000000 * multiplier * 0.5  # Minimum varies by city
        max_price = 30000000 * multiplier       # Maximum varies by city
        final_price = np.clip(final_price, min_price, max_price)
        
        data.append({
            'sizes': int(size),
            'bedrooms': int(bedrooms),
            'city': city,
            'prices': int(final_price)
        })
    
    return pd.DataFrame(data)


def train_and_save_model():
    """Train model with proper dataset, validation, and location parameter"""
    print("🏠 Training Enhanced Indian House Price Prediction Model...")
    print("=" * 60)
    
    # Generate realistic dataset with location data
    df = generate_realistic_indian_housing_data(1000)
    print(f"✅ Generated {len(df)} realistic Indian house data points")
    print(f"📍 Cities included: {', '.join(df['city'].unique())}")
    
    # Encode city names to numbers for machine learning
    label_encoder = LabelEncoder()
    df['city_encoded'] = label_encoder.fit_transform(df['city'])
    
    # Split features and target (now includes location!)
    X = df[["sizes", "bedrooms", "city_encoded"]]
    y = df["prices"]
    
    print(f"\n📊 Features used for prediction:")
    print(f"   1. House Size (sq ft)")
    print(f"   2. Number of Bedrooms") 
    print(f"   3. City/Location (encoded)")
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"\n📊 Training samples: {len(X_train)}")
    print(f"📊 Testing samples: {len(X_test)}")
    
    # Train the model
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    
    # Evaluate the model
    y_train_pred = reg.predict(X_train)
    y_test_pred = reg.predict(X_test)
    
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    
    print(f"\n🎯 Enhanced Model Performance:")
    print(f"   Training R² Score: {train_r2:.4f}")
    print(f"   Testing R² Score: {test_r2:.4f}")
    print(f"   Testing RMSE: ₹{test_rmse:,.2f}")
    
    if test_r2 > 0.8:
        print("✅ Model performs well!")
    else:
        print("⚠️ Model needs improvement")
    
    # Save the improved model and city encoder
    with open("model.pkl", "wb") as f:
        pickle.dump(reg, f)
    
    with open("city_encoder.pkl", "wb") as f:
        pickle.dump(label_encoder, f)
    
    print("💾 Enhanced Indian housing model saved as 'model.pkl'")
    print("💾 City encoder saved as 'city_encoder.pkl'")
    
    # Demonstrate location impact
    print(f"\n🏙️ LOCATION IMPACT DEMO (1200 sq ft, 3 BHK):")
    print("-" * 50)
    
    for city in ['Mumbai', 'Delhi', 'Bangalore', 'Pune', 'Ahmedabad']:
        city_encoded = label_encoder.transform([city])[0]
        features = pd.DataFrame({
            "sizes": [1200],
            "bedrooms": [3], 
            "city_encoded": [city_encoded]
        })
        
        prediction = reg.predict(features)[0]
        if prediction >= 10000000:
            formatted_price = f"₹{prediction/10000000:.2f} Cr"
        elif prediction >= 100000:
            formatted_price = f"₹{prediction/100000:.2f} L"
        else:
            formatted_price = f"₹{prediction:,.0f}"
            
        print(f"📍 {city:10}: {formatted_price}")
    
    return reg, label_encoder


if __name__ == "__main__":
    train_and_save_model()
