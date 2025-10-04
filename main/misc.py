# Inside data.py or misc.py
import pandas as pd

def load_data():
    """Loads the Boston Housing dataset from a local CSV file."""
    file_path = r"D:\mlops_assignment_1\housing.csv"  
    
   
    df = pd.read_csv(file_path)
    
    return df
feature_names = [
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
    'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
]

df = pd.read_csv(file_path, names=feature_names, header=None)

