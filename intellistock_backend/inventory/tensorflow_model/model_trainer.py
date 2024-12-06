import tensorflow as tf
from tensorflow.keras import layers, models
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Function to load and preprocess sales data
def load_and_preprocess_data(csv_file_path):
    """
    Load and preprocess sales data from CSV.
    Features: quantity_on_hand, unit_cost, reorder_point, etc.
    Label: suggested_quantity_to_order.
    """
    data = pd.read_csv(csv_file_path)
    
    # Select relevant columns for features and labels
    features = data[['quantity_on_hand', 'unit_cost', 'reorder_point', 'perishability', 'vendor_lead_time_days']]
    labels = data['suggested_quantity_to_order']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    # Normalize the features using StandardScaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test, scaler

# Define the TensorFlow model
def build_model(input_shape):
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(input_shape,)),  # Input layer
        layers.Dropout(0.2),  # Dropout to prevent overfitting
        layers.Dense(64, activation='relu'),  # Hidden layer
        layers.Dense(1)  # Output layer (suggested_quantity_to_order)
    ])
    
    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    return model

# Function to train the model
def train_model(csv_file_path, model_save_path):
 
    # Load and preprocess data
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data(csv_file_path)
    
    # Build the model
    model = build_model(X_train.shape[1])
    
    # Train the model
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
    
    # Save the trained model to a file
    model.save(model_save_path)
    
    # Save the scaler for future use
    return scaler

# Function to predict the suggested quantity to order using the trained model
def predict_quantity(input_data, model_path, scaler):
    """
    Predict the suggested quantity to order using the trained model and input data.
    """
    # Preprocess the input data
    input_data = scaler.transform([input_data])  # Standardize input using saved scaler
    
    # Load the saved model
    model = tf.keras.models.load_model(model_path)
    
    # Make prediction
    predicted_quantity = model.predict(input_data)
    
    return predicted_quantity[0][0]

if __name__ == "__main__":
    # Path to sales data CSV and model save path
    sales_data_csv = 'path_to_sales_data.csv'
    model_save_path = 'suggested_quantity_model.h5'
    
    # Train the model
    print("Training the model...")
    scaler = train_model(sales_data_csv, model_save_path)

    item_data = [150, 5.50, 100, 1, 7]  # Example data: quantity_on_hand, unit_cost, reorder_point, perishability, vendor_lead_time_days
    print(f"Predicting suggested quantity to order for item data: {item_data}")
    predicted_quantity = predict_quantity(item_data, model_save_path, scaler)
    
    print(f"Suggested Quantity to Order: {predicted_quantity}")
