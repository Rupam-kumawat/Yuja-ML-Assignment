# dataclean.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    data[['Longitude', 'Latitude']] = data['Longitude;Latitude'].str.split(';', expand=True)
    data = data[['Longitude', 'Latitude']]
    data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')
    data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
    data_cleaned = data.drop_duplicates().dropna()
    return data_cleaned

def scale_data(data_cleaned):
    scaler = StandardScaler()
    return scaler.fit_transform(data_cleaned)
