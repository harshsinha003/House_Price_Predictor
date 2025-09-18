import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [value, setValue] = useState("Loading...");
  const [value2, setValue2] = useState({
    sizes: [],
    bedrooms: [],
  });
  const [inputSize, setInputSize] = useState("");
  const [inputBedrooms, setInputBedrooms] = useState("");
  const [inputCity, setInputCity] = useState("Delhi");
  const [price, setPrice] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  // Comprehensive Indian cities for selection
  const indianCities = [
    // Tier-1 Metropolitan Cities
    "Mumbai", "Delhi", "Bangalore", "Pune", "Chennai", "Hyderabad", "Kolkata",
    
    // Tier-1 Major Cities  
    "Ahmedabad", "Surat", "Noida", "Gurgaon", "Ghaziabad", "Faridabad",
    
    // Tier-2 State Capitals & Major Cities
    "Jaipur", "Lucknow", "Indore", "Bhopal", "Kochi", "Coimbatore", "Nagpur",
    "Visakhapatnam", "Thiruvananthapuram", "Bhubaneswar", "Chandigarh",
    
    // Tier-2 Industrial & Tech Hubs
    "Mysore", "Nashik", "Vadodara", "Rajkot", "Kanpur", "Ludhiana", "Agra",
    
    // Tier-3 Emerging Cities
    "Guwahati", "Patna", "Raipur", "Dehradun", "Jammu", "Amritsar", "Jalandhar"
  ].sort(); // Sort alphabetically for better UX

  const fetchValue = async () => {
    if (!inputSize || !inputBedrooms || !inputCity) {
      setError("Please fill in all fields");
      return;
    }
    
    setIsLoading(true);
    setError("");
    
    try {
      const requestData = {
        sizes: [Number(inputSize)],
        bedrooms: [Number(inputBedrooms)],
        cities: [inputCity]
      };
      
      const res = await axios.post(
        "http://localhost:5000/api/predict/",
        requestData
      );
      console.log(res.data.results[0].predicted_price);
      setPrice(res.data.results[0].predicted_price);
    } catch (error) {
      console.log("Error:", error.message);
      setError("Failed to get prediction. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const resetForm = () => {
    setInputSize("");
    setInputBedrooms("");
    setInputCity("Delhi");
    setPrice("");
    setError("");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <div className="container mx-auto px-4 py-8">
        <div className="text-center mb-12">
          <h1 className="text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 mb-4">
            🏠 Indian House Price Predictor
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Get instant house price predictions based on size and number of bedrooms using our advanced AI model
          </p>
        </div>

        {/* Main Card */}
        <div className="max-w-4xl mx-auto">
          <div className="bg-white rounded-3xl shadow-2xl p-8 md:p-12">
            {/* Input Section */}
            <div className="grid md:grid-cols-3 gap-6 mb-8">
              {/* House Size Input */}
              <div className="space-y-2">
                <label className="text-lg font-semibold text-gray-700 flex items-center gap-2">
                  📐 House Size
                </label>
                <div className="relative">
                  <input
                    type="number"
                    value={inputSize}
                    placeholder="e.g., 1200"
                    className="input input-bordered w-full h-14 text-lg pl-4 pr-16 border-2 border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 rounded-xl"
                    onChange={(e) => setInputSize(e.target.value)}
                  />
                  <span className="absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-500 font-medium">
                    sq ft
                  </span>
                </div>
              </div>

              {/* Bedrooms Input */}
              <div className="space-y-2">
                <label className="text-lg font-semibold text-gray-700 flex items-center gap-2">
                  🛏️ Number of Bedrooms
                </label>
                <input
                  type="number"
                  value={inputBedrooms}
                  placeholder="e.g., 3"
                  min="1"
                  max="10"
                  className="input input-bordered w-full h-14 text-lg px-4 border-2 border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 rounded-xl"
                  onChange={(e) => setInputBedrooms(e.target.value)}
                />
              </div>

              {/* City Selection */}
              <div className="space-y-2">
                <label className="text-lg font-semibold text-gray-700 flex items-center gap-2">
                  🏙️ City/Location
                </label>
                <select
                  value={inputCity}
                  className="select select-bordered w-full h-14 text-lg px-4 border-2 border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 rounded-xl"
                  onChange={(e) => setInputCity(e.target.value)}
                >
                  {indianCities.map((city) => (
                    <option key={city} value={city}>
                      {city}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {/* Error Message */}
            {error && (
              <div className="alert alert-error mb-6 rounded-xl">
                <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span>{error}</span>
              </div>
            )}

            {/* Action Buttons */}
            <div className="flex gap-4 justify-center mb-8">
              <button 
                className={`btn btn-primary btn-lg px-8 h-14 text-lg rounded-xl ${isLoading ? 'loading' : ''}`}
                onClick={fetchValue}
                disabled={isLoading}
              >
                {isLoading ? 'Predicting...' : '🔮 Predict Price'}
              </button>
              <button 
                className="btn btn-outline btn-lg px-8 h-14 text-lg rounded-xl"
                onClick={resetForm}
              >
                🔄 Reset
              </button>
            </div>

            {/* Result Section */}
            {price && (
              <div className="bg-gradient-to-r from-green-50 to-emerald-50 border-2 border-green-200 rounded-3xl p-8 text-center">
                <h2 className="text-2xl font-bold text-gray-800 mb-4">
                  🎉 Prediction Result
                </h2>
                <div className="bg-white rounded-2xl p-6 shadow-lg">
                  <p className="text-lg text-gray-600 mb-2">Estimated House Price</p>
                  <p className="text-5xl font-bold text-green-600 mb-4">
                    {price}
                  </p>
                  <div className="grid grid-cols-3 gap-4 text-sm text-gray-500">
                    <div className="bg-gray-50 rounded-lg p-3">
                      <p className="font-semibold">Size</p>
                      <p>{inputSize} sq ft</p>
                    </div>
                    <div className="bg-gray-50 rounded-lg p-3">
                      <p className="font-semibold">Bedrooms</p>
                      <p>{inputBedrooms} rooms</p>
                    </div>
                    <div className="bg-gray-50 rounded-lg p-3">
                      <p className="font-semibold">Location</p>
                      <p>{inputCity}</p>
                    </div>
                  </div>
                  <div className="mt-4 text-xs text-gray-400">
                    *Prices based on Indian real estate market
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Features Section */}
          <div className="grid md:grid-cols-3 gap-6 mt-12">
            <div className="bg-white rounded-2xl p-6 shadow-lg text-center">
              <div className="text-4xl mb-4">⚡</div>
              <h3 className="text-xl font-bold text-gray-800 mb-2">Instant Results</h3>
              <p className="text-gray-600">Get predictions in seconds using our trained AI model</p>
            </div>
            <div className="bg-white rounded-2xl p-6 shadow-lg text-center">
              <div className="text-4xl mb-4">🎯</div>
              <h3 className="text-xl font-bold text-gray-800 mb-2">Accurate Predictions</h3>
              <p className="text-gray-600">Based on machine learning algorithms and market data</p>
            </div>
            <div className="bg-white rounded-2xl p-6 shadow-lg text-center">
              <div className="text-4xl mb-4">🔒</div>
              <h3 className="text-xl font-bold text-gray-800 mb-2">Secure & Private</h3>
              <p className="text-gray-600">Your data is processed securely and not stored</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
