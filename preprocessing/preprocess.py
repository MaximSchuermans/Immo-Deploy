import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from pickle import load

scaler = load(open('./preprocessing/scaler.pkl', 'rb'))

def preprocess(data):
    # Handle categorical variables
    data_encoded = pd.DataFrame.from_dict(data)
    print("Data: ", data)
    print("Data encoded: ", data_encoded)
    categorical_columns = ['Type of property', 'Subtype of property', 'Type of sale', 'State of the building', 'Compound Listing']
    data_encoded = pd.get_dummies(pd.DataFrame.from_dict(data), columns=categorical_columns, drop_first=True)
    # Normalize numerical features
    numerical_columns = [
        'Locality', 'Garden area', 'Surface of the land', 'Surface area of the plot of land',
        'Number of rooms', 'Living Area', 'Terrace area', 'Number of facades'
    ]
    data_encoded[numerical_columns] = scaler.fit_transform(data_encoded[numerical_columns])
    return data_encoded
