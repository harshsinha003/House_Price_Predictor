# 🏠 House_Price_Predictior

AI-powered house price prediction system for the Indian real estate market using React and Python.

## ✨ Features

- 🇮🇳 **38+ In```
House_Price_Predictior/
├── 📄 README.md                    # Project documentation
├── 📄 .gitignore                   # Git ignore rules
├── 🔥 app.py                       # Flask API server
├── 🔥 train_model.py               # Model training scriptities Support** - Comprehensive coverage across all major cities
- 🏙️ **Location-Based Pricing** - City-specific price multipliers for accurate predictions
- ₹ **Indian Currency Formatting** - Displays prices in Lakhs and Crores
- 📱 **Modern React UI** - Beautiful, responsive interface with Tailwind CSS
- 🤖 **Machine Learning Predictions** - Linear Regression model with 84% accuracy
- 📊 **Real-time API** - Fast Flask backend with comprehensive error handling

## 🛠️ Tech Stack

### Backend
- **Python 3.11** - Core programming language
- **Flask** - Lightweight web framework
- **Scikit-learn** - Machine learning library
- **Pandas & NumPy** - Data processing
- **Pickle** - Model serialization

### Frontend
- **React 18** - Modern UI framework
- **Vite** - Fast build tool
- **Tailwind CSS** - Utility-first CSS framework
- **DaisyUI** - Beautiful UI components
- **Axios** - HTTP client for API calls

### Machine Learning
- **Linear Regression** - Core prediction algorithm
- **Label Encoding** - City categorization
- **Train/Test Split** - Proper validation methodology

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Clone the repository**
```bash
git clone https://github.com/harshsinha003/House_Price_Predictior.git
cd House_Price_Predictior
```

2. **Create virtual environment**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Start the Flask server**
```bash
python app.py
```
Backend will be available at `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm run dev
```
Frontend will be available at `http://localhost:5173`

## 📊 Model Performance

- **Accuracy (R² Score)**: 84%
- **RMSE**: ₹55,000
- **Training Data**: 1,000 realistic samples
- **Features**: House size, bedrooms, location
- **Location Impact**: Up to 1.2x price variation between cities

## 🏙️ Supported Cities

### Tier-1 Metropolitan Cities (7)
Mumbai, Delhi, Bangalore, Pune, Chennai, Hyderabad, Kolkata

### Tier-1 Major Cities (6)
Ahmedabad, Surat, Noida, Gurgaon, Ghaziabad, Faridabad

### Tier-2 State Capitals & Major Cities (11)
Jaipur, Lucknow, Indore, Bhopal, Kochi, Coimbatore, Nagpur, Visakhapatnam, Thiruvananthapuram, Bhubaneswar, Chandigarh

### Tier-2 Industrial & Tech Hubs (7)
Mysore, Nashik, Vadodara, Rajkot, Kanpur, Ludhiana, Agra

### Tier-3 Emerging Cities (7)
Guwahati, Patna, Raipur, Dehradun, Jammu, Amritsar, Jalandhar

## 📡 API Documentation

### Predict House Price
**POST** `/api/predict/`

**Request Body:**
```json
{
  "sizes": [1200],
  "bedrooms": [3],
  "cities": ["Mumbai"]
}
```

**Response:**
```json
{
  "message": "Prediction results",
  "results": [
    {
      "size": 1200,
      "bedroom": 3,
      "city": "Mumbai",
      "predicted_price": "₹87.21 L",
      "predicted_price_raw": 8721000
    }
  ]
}
```

## 🎯 Example Predictions

| House Type | Size | Location | Predicted Price |
|------------|------|----------|----------------|
| 1BHK | 600 sq ft | Mumbai | ₹40.55 L |
| 2BHK | 900 sq ft | Delhi | ₹63.88 L |
| 3BHK | 1200 sq ft | Bangalore | ₹99.81 L |
| 4BHK | 1800 sq ft | Pune | ₹1.35 Cr |

## 🧪 Testing

### API Testing
```bash
python test_api.py
```

### Location Impact Demo
```bash
python location_impact_demo.py
```

## 📁 Project Structure

```
House_Price_Predictor/
├── � README.md                    # Project documentation
├── 📄 .gitignore                   # Git ignore rules
├── 🔥 app.py                       # Flask API server
├── 🔥 train_model.py               # Model training script
├── 🔥 improved_train_model.py      # Enhanced training
├── 🔥 enhanced_model_with_location.py # Location-aware training
├── 🔥 model.pkl                    # Trained ML model
├── 🔥 city_encoder.pkl             # City encoder
├── 📄 requirements.txt             # Python dependencies
├── 🧪 test_api.py                  # API testing script
├── 🧪 location_impact_demo.py      # Location feature demo
└── 📁 frontend/                    # React application
    ├── 📄 package.json             # Node dependencies
    ├── 📄 index.html               # Main HTML
    ├── 📁 src/                     # React source code
    │   ├── 📄 App.jsx              # Main component
    │   ├── 📄 main.jsx             # Entry point
    │   └── 📄 index.css            # Styles
    └── 📁 public/                  # Static assets
```

## 🚀 Deployment

### Backend (Heroku)
1. Create `Procfile`: `web: python app.py`
2. Create `runtime.txt`: `python-3.11.0`
3. Deploy to Heroku

### Frontend (Netlify)
1. Build command: `npm run build`
2. Publish directory: `dist`
3. Deploy to Netlify

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Harsh Sinha** - [GitHub](https://github.com/harshsinha003)

## 🙏 Acknowledgments

- Scikit-learn for machine learning capabilities
- React team for the amazing frontend framework
- Tailwind CSS for beautiful styling
- Indian real estate market data inspiration

---

⭐ **Star this repository if you found it helpful!**
