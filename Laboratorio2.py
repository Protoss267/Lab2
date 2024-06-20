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

droping_colsC=[]
for col in DF_cleveland.columns:
    maxScore=0
    for sel_col in select_colum:
        if(similar(col,sel_col)>maxScore):
            maxScore= similar(col,sel_col)
    if(maxScore<0.7):
        droping_colsC.append(col)
    else:
        if('previous' in col):
            droping_colsC.append(col)

DF_cleveland.drop(columns=droping_colsC,inplace=True)
DF_cleveland.head(1)

droping_colsH=[]
for col in DF_hungarian.columns:
    maxScore=0
    for sel_col in select_colum:
        if(similar(col,sel_col)>maxScore):
            maxScore= similar(col,sel_col)
    if(maxScore<0.7):
        droping_colsH.append(col)
    else:
        if('previous' in col):
            droping_colsH.append(col)

DF_hungarian.drop(columns=droping_colsH,inplace=True)
DF_hungarian.head(1)

droping_colsS=[]
for col in DF_switzerland.columns:
    maxScore=0
    for sel_col in select_colum:
        if(similar(col,sel_col)>maxScore):
            maxScore= similar(col,sel_col)
    if(maxScore<0.7):
        droping_colsS.append(col)
    else:
        if('previous' in col):
            droping_colsS.append(col)

DF_switzerland.drop(columns=droping_colsS,inplace=True)
DF_switzerland.head(1)
in_df= pd.concat([DF_cleveland,DF_hungarian,DF_switzerland])
in_df.reset_index(inplace=True)
in_df.drop(columns=['index'],inplace= True)
in_df.head(1)

