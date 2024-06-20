import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error, r2_score

with open('houseprices_reg.pkl', 'rb') as f:
    houseprices_model = pickle.load(f)
houseprices_data = pd.read_csv('houseprices_regression.csv')

print(houseprices_data)
