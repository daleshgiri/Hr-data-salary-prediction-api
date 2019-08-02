import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pickle
import os
def pre_proc(df):
    df.drop(['last_evaluation', 'number_project'], axis='columns', inplace=True)
    df["salary"].replace(["low", "medium", "high"], [0,1,2], inplace=True)
    df = pd.get_dummies(df)
    df["average_montly_hours"] = pd.cut(df["average_montly_hours"], bins=[0,150,200,1000], labels=[2,1,3])
    df["time_spend_company"] = pd.cut(df["time_spend_company"], bins=[0,2,5, 1000], labels=[3,2,1])
    df["average_montly_hours"] = df["average_montly_hours"].astype('int64') 
    df["time_spend_company"] = df["time_spend_company"].astype('int64') 
    return df

def training(df):
    df = pre_proc(df)
    y = df["left"]
    df.drop("left", axis="columns", inplace=True)
    X = df
    
    dummyRow = pd.DataFrame(np.zeros(len(X.columns)).reshape(1, len(X.columns)), columns=X.columns)    
    dummyRow.to_csv("dummyRow.csv", index=False)

    model = RandomForestClassifier()    
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
    model.fit(X, y)
    
    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)
    
    print(model.score(X,y))
    yp = model.predict(X)
    print("left", sum(yp!=0))
    print("not left", sum(yp==0))
    cm = confusion_matrix(y, yp)
    print(cm)


# In[ ]:


def pred(ob):
    d1 = ob.to_dict()
    df = pd.DataFrame(d1, index=[0])
    df.drop("left", axis="columns", inplace=True)    
    df = pre_proc(df)
    dummyrow_filename = "dummyRow.csv"
    dummyrow_filename = os.path.dirname(__file__) + "/" + dummyrow_filename    
    df2 = pd.read_csv(dummyrow_filename)    
    for c1 in df.columns:
        df2[c1] = df[c1]
    pkl_filename = "pickle_model.pkl"
    pkl_filename = os.path.dirname(__file__) + "/" + pkl_filename
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict(df2)
    return pred

if __name__ == "__main__":
    df = pd.read_csv("HR_comma_sep.csv")
    training(df)    


