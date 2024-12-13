import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from pickle import load
import joblib

preprocessor = joblib.load('./preprocessing/preprocessor.pkl')

def preprocess(row):
    new_data = pd.DataFrame(row, index=[0])
    preprocessed_data = preprocessor.transform(new_data)
    return row, new_data, preprocessed_data

