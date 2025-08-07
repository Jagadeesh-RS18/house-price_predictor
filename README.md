# 🏠 House Price Predictor

This is a simple **Machine Learning web app** that predicts house prices based on input features like number of bedrooms, bathrooms, square footage, and location. The project uses a **Scikit-learn regression model**, built with **Python**, **Flask**, **HTML/CSS**, and deployed locally.

---

## 📂 Project Structure

house-price-predictor/
├── app/
│ ├── app.py # Flask backend
│ └── templates/
│ ├── index.html # Input form page
│ └── result.html # Prediction result page
├── static/
│ ├── css/
│ │ └── style.css # Styling for UI
│ └── images/
│──train_model.py 
├── model/
│ └── model.pkl # Trained ML model
├── data/
│ └── house_data.csv # Dataset used for training
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- HTML5 & CSS3
- Scikit-learn
- Pandas & NumPy
- Matplotlib / Seaborn (for EDA)
- Bootstrap (optional)

---

## 🚀 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

pip install -r requirements.txt
cd app
python app.py
