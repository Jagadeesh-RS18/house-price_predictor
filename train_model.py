# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle
import os

# Step 1: Load the dataset
data_path = os.path.join('data', 'house_data.csv')
df = pd.read_csv(data_path)

# Step 2: Prepare Features and Target
X = df[['Area', 'Bedrooms', 'Bathrooms', 'Location']]
y = df['Price']

# Step 3: One-Hot Encode the 'Location' feature
preprocessor = ColumnTransformer([
    ('location_encoder', OneHotEncoder(handle_unknown='ignore'), ['Location'])
], remainder='passthrough')  # Keep Area, Bedrooms, Bathrooms as they are

# Step 4: Create a Pipeline (Preprocessing + Linear Regression)
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Step 5: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Fit the Model
model.fit(X_train, y_train)

# Step 7: Save the trained model
output_path = os.path.join('model', 'model.pkl')
pickle.dump(model, open(output_path, 'wb'))

print("✅ Model trained and saved to:", output_path)
