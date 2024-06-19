import pandas as pd
from difflib import SequenceMatcher

def similar(input1,input2):
    return SequenceMatcher(None,input1,input2).ratio()

DF_cleveland =pd.read_csv('heart-disease.cleveland.csv')
DF_hungarian= pd.read_csv('heart-disease.hungarian.csv')
DF_switzerland= pd.read_csv('heart-disease.switzerland.csv')


print(DF_hungarian.shape)
print(DF_cleveland.shape)
print(DF_switzerland.shape)

colum= pd.DataFrame(False,index=DF_cleveland.columns,columns=['H','C','S'])
colum.C = True

for col in DF_hungarian.columns:
    for incol in colum.index:
        if(similar(col,incol)>0.7):
            colum.at[incol,'H']=True

for col in DF_switzerland.columns:
    for incol in colum.index:
        if(similar(col,incol)>0.7):
            colum.at[incol,'S']=True

colum[colum.H & colum.C & colum.S]
print(colum)

select_colum = [
    'age',
    'sex',
    'cp',
    'trestbps',
    'chol',
    'fbs',
    'restecg',
    'thalach',
    'exang',
    'oldpeak',
    'slope',
    'ca',
    'thal',
    'num'
]
