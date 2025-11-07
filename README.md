# House Price Predictor

A machine learning-based web application that predicts house prices for the Indian real estate market using advanced algorithms and location-based pricing.

## 🏠 Features

- **ML-Powered Predictions**: Uses scikit-learn with 84% accuracy
- **React Frontend**: Modern, responsive user interface
- **Flask API Backend**: RESTful API for price predictions
- **38+ Indian Cities**: Comprehensive location-based pricing
- **Real-time Predictions**: Instant price estimates
- **Indian Currency Format**: Results in Lakhs/Crores

## 🌐 Try the website
[Click here to try it out](https://house-price-predictor-snowy.vercel.app)


## 🛠️ Tech Stack

**Backend:**
- Python Flask
- scikit-learn
- Pandas & NumPy
- Flask-CORS

**Frontend:**
- React.js
- Modern ES6+
- Responsive Design

**Machine Learning:**
- Linear Regression Model
- Feature Engineering
- Location-based Multipliers
- Data Preprocessing

## 🚀 Installation & Setup

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/harshsinha003/House_Price_Predictor.git
cd House_Price_Predictor

# Install dependencies
pip install -r requirements.txt

# Run the Flask API
python app.py
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 📁 Project Structure

```
House_Price_Predictor/
├── app.py                           # Flask API server
├── train_model.py                   # Model training script
├── enhanced_model_with_location.py  # Advanced model with location features
├── model.pkl                        # Trained ML model
├── city_encoder.pkl                 # City encoding for predictions
├── requirements.txt                 # Python dependencies
├── frontend/                        # React application
│   ├── src/
│   ├── package.json
│   └── ...
└── README.md
```

## 📊 Model Performance

- **Algorithm**: Linear Regression
- **Accuracy**: 84%
- **Features**: Location, size, amenities, market trends
- **Supported Cities**: 38+ Indian cities including Mumbai, Delhi, Bangalore
- **Dataset**: Indian real estate market data

## 🌟 API Endpoints

### Predict House Price
```
POST /predict
Content-Type: application/json

{
  "location": "Mumbai",
  "total_sqft": 1200,
  "bath": 2,
  "bhk": 3
}
```

### Response
```json
{
  "predicted_price": "45.67 Lakh",
  "location": "Mumbai",
  "details": {
    "sqft": 1200,
    "bathrooms": 2,
    "bedrooms": 3
  }
}
```

## 🔧 Key Features

### Machine Learning Model
- **Training Data**: Comprehensive Indian real estate dataset
- **Preprocessing**: Feature scaling, categorical encoding
- **Validation**: Cross-validation with 84% accuracy
- **Location Intelligence**: City-specific price multipliers

### Frontend Features
- **Responsive Design**: Works on desktop and mobile
- **Real-time Validation**: Input validation and error handling
- **Interactive UI**: Clean, modern interface
- **Instant Results**: Fast prediction response

### Backend API
- **RESTful Design**: Clean API endpoints
- **Error Handling**: Comprehensive error responses
- **CORS Support**: Frontend-backend communication
- **Model Loading**: Efficient pickle model loading

## 🧪 Testing

```bash
# Test the API
python test_api.py

# Run model training
python train_model.py

# Test enhanced model
python enhanced_model_with_location.py
```

## 📈 Model Training

The model is trained on features including:
- **Location**: City-based pricing variations
- **Size**: Total square feet area
- **Bedrooms**: Number of BHK
- **Bathrooms**: Number of bathrooms
- **Market Trends**: Historical price data

## 🌐 Deployment

This application can be deployed on:
- **Heroku**: For the Flask backend
- **Netlify/Vercel**: For the React frontend
- **Railway**: Full-stack deployment
- **Docker**: Containerized deployment

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Harsh Sinha** (@harshsinha003)
- GitHub: [harshsinha003](https://github.com/harshsinha003)
- Email: harshvardhansinha88@gmail.com

## 🙏 Acknowledgments

- Indian real estate market data providers
- scikit-learn community
- React.js developers
- Flask framework contributors

---


⭐ **If you found this project helpful, please give it a star!** ⭐

