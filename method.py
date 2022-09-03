import pandas as pd
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.impute import SimpleImputer as SI
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

def label_with_LE(df):
    object_col = [col for col in df.columns if df[col].dtype == "object"]
    label_encoder = LE()
    df[object_col] = label_encoder.fit_transform(df[object_col])

    return df

def impute_col(df):
    impute = SI()
    imputed_df = pd.DataFrame(impute.fit_transform(df))
    imputed_df.columns = df.columns
    
    return imputed_df