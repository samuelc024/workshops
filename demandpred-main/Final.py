import numpy as np
import pandas as pd

final_types1 = {'WeekNumber': np.uint8,
                'NewClientName': np.int64,
                'NewProductName': np.float64,
                'pieces':np.float64,
                'weight':np.float64,
                'brand':np.int64,
                'Town':np.int64,
                'State':np.int64,
                'MeanR':np.float64,
                'MeanSC':np.float64,
                'MeanSD':np.float64,
                'MeanP':np.float64,
                'MeanC':np.float64,
                'MeanPSD':np.float64,
                'MeanPSC':np.float64,
                'MeanPR':np.float64,
                'MeanPC':np.float64,
                'MeanPCSC':np.float64,
                'MeanPCSD':np.float64,
                }

final_types = {'WeekNumber': np.uint8,
                'SalesDepotID': np.uint16,
                'SalesChannelID':np.uint8,
                'RouteID':np.uint16,
                'ClientID':np.uint32,
                'ProductID':np.uint16,
                'Demand':np.uint8,
                'NewClientName': np.object,
                'NewProductName': np.object,
                'pieces':np.float64,
                'weight':np.float64,
                'brand':np.object,
                'Town':np.object,
                'State':np.object
                }

def map_kaggle_to_model_columns(df, is_train=True):
    """Mapea los nombres de columnas de Kaggle a los nombres que usa tu modelo"""
    
    column_mapping = {
        'Semana': 'WeekNumber',
        'Agencia_ID': 'SalesDepotID',
        'Canal_ID': 'SalesChannelID',
        'Ruta_SAK': 'RouteID',
        'Cliente_ID': 'ClientID',
        'Producto_ID': 'ProductID'
    }
    
    if is_train:
        column_mapping['Demanda_uni_equil'] = 'Demand'
    
    df = df.rename(columns=column_mapping)
    
  
    extra_columns = {
        'NewClientName': 'unknown',
        'NewProductName': 'unknown',
        'pieces': 0.0,
        'weight': 0.0,
        'brand': 'unknown_brand',
        'Town': 'unknown_town',
        'State': 'unknown_state'
    }
    
    for col, default_val in extra_columns.items():
        if col not in df.columns:
            df[col] = default_val
    
    return df

def mean_encoding_unique_categorical_features_on_traindata(train):

  MeanR = train.groupby(['RouteID'], as_index=False)['Demand'].mean()
  MeanSC = train.groupby(['SalesChannelID'], as_index=False)['Demand'].mean()
  MeanSD = train.groupby(['SalesDepotID'], as_index=False)['Demand'].mean()
  MeanP = train.groupby(['ProductID'], as_index=False)['Demand'].mean()
  MeanC = train.groupby(['ClientID'], as_index=False)['Demand'].mean()
  MeanPSD = train.groupby(['ProductID','SalesDepotID'], as_index=False)['Demand'].mean()
  MeanPSC = train.groupby(['ProductID','SalesChannelID'], as_index=False)['Demand'].mean()
  MeanPR = train.groupby(['ProductID','RouteID'], as_index=False)['Demand'].mean()
  MeanPC = train.groupby(['ProductID','ClientID'], as_index=False)['Demand'].mean()
  MeanPCSC = train.groupby(['ProductID','ClientID','SalesChannelID'], as_index=False)['Demand'].mean()
  MeanPCSD = train.groupby(['ProductID','ClientID','SalesDepotID'], as_index=False)['Demand'].mean()
  temp=[MeanR,MeanSC,MeanSD,MeanP,MeanC,MeanPSD,MeanPSC,MeanPR,MeanPC,MeanPCSC,MeanPCSD]

  return temp

import pandas as pd
def merge_newfeatures_of_unique_categorical_data(temp,train_test):
  MeanR=pd.DataFrame(temp[0])
  MeanSC=pd.DataFrame(temp[1])
  MeanSD=pd.DataFrame(temp[2])
  MeanP=pd.DataFrame(temp[3])
  MeanC=pd.DataFrame(temp[4])
  MeanPSD=pd.DataFrame(temp[5])
  MeanPSC=pd.DataFrame(temp[6])
  MeanPR=pd.DataFrame(temp[7])
  MeanPC=pd.DataFrame(temp[8])
  MeanPCSC=pd.DataFrame(temp[9])
  MeanPCSD=pd.DataFrame(temp[10])
  MeanR.rename(columns = {'Demand':'MeanR'}, inplace = True)
  MeanSC.rename(columns = {'Demand':'MeanSC'}, inplace = True)
  MeanSD.rename(columns = {'Demand':'MeanSD'}, inplace = True)
  MeanP.rename(columns = {'Demand':'MeanP'}, inplace = True)
  MeanC.rename(columns = {'Demand':'MeanC'}, inplace = True)
  MeanPSD.rename(columns = {'Demand':'MeanPSD'}, inplace = True)
  MeanPSC.rename(columns = {'Demand':'MeanPSC'}, inplace = True)
  MeanPR.rename(columns = {'Demand':'MeanPR'}, inplace = True)
  MeanPC.rename(columns = {'Demand':'MeanPC'}, inplace = True)
  MeanPCSC.rename(columns = {'Demand':'MeanPCSC'}, inplace = True)
  MeanPCSD.rename(columns = {'Demand':'MeanPCSD'}, inplace = True)
  final_data=pd.merge(train_test,MeanR.astype(object),how = 'left', on='RouteID')
  final_data=pd.merge(final_data,MeanSC.astype(object),how = 'left', on='SalesChannelID')
  final_data=pd.merge(final_data,MeanSD.astype(object),how = 'left', on='SalesDepotID')
  final_data=pd.merge(final_data,MeanP.astype(object),how = 'left', on='ProductID')
  final_data=pd.merge(final_data,MeanC.astype(object),how = 'left', on='ClientID')
  final_data=pd.merge(final_data,MeanPSD.astype(object),how = 'left', on=['ProductID','SalesDepotID'])
  final_data=pd.merge(final_data,MeanPSC.astype(object),how = 'left', on=['ProductID','SalesChannelID'])
  final_data=pd.merge(final_data,MeanPR.astype(object),how = 'left', on=['ProductID','RouteID'])
  final_data=pd.merge(final_data,MeanPC.astype(object),how = 'left', on=['ProductID','ClientID'])
  final_data=pd.merge(final_data,MeanPCSC.astype(object),how = 'left', on=['ProductID','ClientID','SalesChannelID'])
  final_data=pd.merge(final_data,MeanPCSD.astype(object),how = 'left', on=['ProductID','ClientID','SalesDepotID'])
  colname=['ProductID','ClientID','SalesDepotID','SalesChannelID','RouteID']
  final_data.drop(colname, axis=1, inplace=True) 
  return final_data

import pickle
def get_dict_of_ordinal_encoding(value_to_convert):
  key=[]
  value=[]
  for k,v in value_to_convert[0].items():
    key.append(k)
    value.append(v)
  value_to_convert1 = [dict(zip(value , key))]
  return value_to_convert1
import pickle

from sklearn.preprocessing import OrdinalEncoder
def vectorize_categorical_text_features_on_train_data(train):
  leNewClientName=OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=-1)
  leNewClientName.fit(train['NewClientName'].values.reshape(-1, 1) )
  
  leNewClientName_map= [dict(enumerate(mapping)) for mapping in leNewClientName.categories_]

  leNewProductName=OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=-1)
  leNewProductName.fit(train['NewProductName'].values.reshape(-1, 1))
  leNewProductName_map = [dict(enumerate(mapping)) for mapping in leNewProductName.categories_]

  leTown=OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=-1)
  leTown.fit(train['Town'].values.reshape(-1, 1) )
  leTown_map = [dict(enumerate(mapping)) for mapping in leTown.categories_]

  leState=OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=-1)
  leState.fit(train['State'].values.reshape(-1, 1))
  leState_map = [dict(enumerate(mapping)) for mapping in leState.categories_]

  lebrand=OrdinalEncoder(handle_unknown='use_encoded_value',unknown_value=-1)
  lebrand.fit(train['brand'].values.reshape(-1, 1))
  lebrand_map = [dict(enumerate(mapping)) for mapping in lebrand.categories_]

  leNewClientName_map1=get_dict_of_ordinal_encoding(leNewClientName_map)
  leNewProductName_map1=get_dict_of_ordinal_encoding(leNewProductName_map)
  leTown_map1=get_dict_of_ordinal_encoding(leTown_map)
  leState_map1=get_dict_of_ordinal_encoding(leState_map)
  lebrand_map1=get_dict_of_ordinal_encoding(lebrand_map)

  temp=[leNewClientName_map1,leNewProductName_map1,leTown_map1,leState_map1,lebrand_map1]

  return temp










def map_categorical_text_features(temp1,train_test):
  leNewClientName_map=temp1[0]
  leNewProductName_map=temp1[1]
  leTown_map=temp1[2]
  leState_map=temp1[3]
  lebrand_map=temp1[4]
  
  train_test['NewClientName']=train_test['NewClientName'].map(leNewClientName_map[0])
  train_test['NewProductName']=train_test['NewProductName'].map(leNewProductName_map[0])
  train_test['Town']=train_test['Town'].map(leTown_map[0])
  train_test['State']=train_test['State'].map(leState_map[0])
  train_test['brand']=train_test['brand'].map(lebrand_map[0])

  return train_test



def preprocess_numerical_data_query(query):
  
  query['pieces']=np.log(int(query['pieces'][0])+1)
  query['weight']=np.log(int(query['weight'][0])+1)
  return query


def safe_convert(df, dtype_map):
    """Conversión segura de tipos con manejo de valores faltantes"""
    for col, dtype in dtype_map.items():
        if col in df.columns:
            if np.issubdtype(dtype, np.integer):
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(dtype)
            else:
                df[col] = df[col].astype(dtype)
    return df

def save_mean_encodings():
    """Guarda las codificaciones medias con manejo de tipos seguro"""
    train = pd.read_csv('train.csv')
    train = map_kaggle_to_model_columns(train, is_train=True)
    train = safe_convert(train, final_types)
    
    encodings = mean_encoding_unique_categorical_features_on_traindata(train)
    with open('mean_encodings.pkl', 'wb') as f:
        pickle.dump(encodings, f)
    print("Mean encodings guardadas correctamente en mean_encodings.pkl")
    
def save_text_encodings():
    """Guarda las codificaciones de texto con manejo de tipos seguro"""
    train = pd.read_csv('train.csv')
    train = map_kaggle_to_model_columns(train, is_train=True)
    train = safe_convert(train, final_types)
    
    temp2 = vectorize_categorical_text_features_on_train_data(train)
    with open('text_encodings.pkl', 'wb') as f:
        pickle.dump(temp2, f)
    print("Text encodings guardadas correctamente en text_encodings.pkl")





def get_expected_features():
    """Devuelve la lista exacta de features que el modelo espera"""
    return [
        'WeekNumber', 'NewClientName', 'NewProductName', 'pieces', 'weight',
        'brand', 'Town', 'State', 'MeanR', 'MeanSC', 'MeanSD', 'MeanP', 'MeanC',
        'MeanPSD', 'MeanPSC', 'MeanPR', 'MeanPC', 'MeanPCSC', 'MeanPCSD'
    ]    

def predict_test_set():
    
    test = pd.read_csv('test.csv')
    
    
    test = map_kaggle_to_model_columns(test, is_train=False)
    
    
    for col in ['NewClientName', 'NewProductName', 'pieces', 'weight', 'brand', 'Town', 'State']:
        if col not in test.columns:
            test[col] = 0 if col in ['pieces', 'weight'] else 'unknown'
    
    
    test['Demand'] = 0  
    
    
    with open('mean_encodings.pkl', 'rb') as f:
        temp1 = pickle.load(f)
    
    with open('text_encodings.pkl', 'rb') as f:
        temp2 = pickle.load(f)
    
    
    test = preprocess_numerical_data_query(test)
    test = merge_newfeatures_of_unique_categorical_data(temp1, test)
    test = map_categorical_text_features(temp2, test)
    
    
    test = test.replace([np.inf, -np.inf], np.nan)
    test = test.fillna(0)  
    
    
    for col, dtype in final_types1.items():
        if col in test.columns:
            if np.issubdtype(dtype, np.integer):
                test[col] = pd.to_numeric(test[col], errors='coerce').fillna(0).astype(dtype)
            else:
                test[col] = test[col].astype(dtype)
    
    
    expected_features = get_expected_features()
    test_features = test[expected_features]
    
   
    final_Model = pickle.load(open('final_model.pkl', 'rb'))
    predictions = final_Model.predict(test_features)
    
    
    submission = pd.DataFrame({
        'id': test['id'],
        'Demanda_uni_equil': np.maximum(np.exp(predictions) - 1, 0).round().astype(int)
    })
    
    submission.to_csv('submission.csv', index=False)
    return submission
