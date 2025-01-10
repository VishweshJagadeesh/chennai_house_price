import json
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

__locations=None
__data_cols=None
__model=None
__scaler=None

def get_estimated_price(area,sale_cond,park_facil,buildtype,utility_avail,street,mzzone,property_age,int_sqft,n_bedroom,n_bathroom,n_room):
    pd.set_option('future.no_silent_downcasting', True)
    test=pd.DataFrame(columns=__data_cols)
    if area in test.columns:
        test.loc[0,area]=1
    if sale_cond in test.columns:
        test.loc[0,sale_cond]=1
    if buildtype in test.columns:
        test.loc[0,buildtype]=1
    if utility_avail in test.columns:
        test.loc[0,utility_avail]=1
    if street in test.columns:
        test.loc[0,street]=1
    if mzzone in test.columns:
        test.loc[0,mzzone]=1
    test.loc[0,'PARK_FACIL']=park_facil
    test.loc[0,'PROPERTY_AGE']=property_age
    test.loc[0,'INT_SQFT']=int_sqft
    test.loc[0,'N_BEDROOM']=n_bedroom
    test.loc[0,'N_BATHROOM']=n_bathroom
    test.loc[0,'N_ROOM']=n_room
    test=test.fillna(0)
    test=__scaler.transform(test)
    return round(__model.predict(test)[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts')
    global __data_cols
    global __locations
    global __model
    global __scaler

    with open(R"C:\Users\vishw\OneDrive\Desktop\CHP\server\artifacts\columns.json",'r') as f:
        __data_cols=json.load(f)['data_columns']
        __locations=__data_cols[7:13]
    with open(R"C:\Users\vishw\OneDrive\Desktop\CHP\server\artifacts\scaler.pickle",'rb') as f:
        __scaler=pickle.load(f)
    with open(R"C:\Users\vishw\OneDrive\Desktop\CHP\server\artifacts\model.pickle",'rb') as f:
        __model=pickle.load(f)
    print("artifacts are done")
if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('anna nagar','family',1,'house','allpub','paved','RM','18',2000,12,12,24))
