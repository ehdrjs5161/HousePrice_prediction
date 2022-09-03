import pandas as pd
import method
import seaborn as sns
from matplotlib import pyplot as plt

def setOptions():
    pd.set_option("display.max_rows", 10)
    pd.set_option('display.max_columns', 100)
    pd.set_option("max_info_columns", 100)

if __name__ == "__main__":
    setOptions()

    data = pd.read_csv("dataSets/train.csv")
    data.drop(columns=['Id'], inplace=True)
    data['Alley'] = data['Alley'].fillna("None")
    data['FireplaceQu'] = data['FireplaceQu'].fillna("None")
    data['GarageType'] = data['GarageType'].fillna(data['GarageType'].value_counts().idxmax())
    data['GarageYrBlt'] = data['GarageYrBlt'].fillna(data['GarageYrBlt'].value_counts().idxmax())
    data['GarageFinish'] = data['GarageFinish'].fillna(data['GarageFinish'].value_counts().idxmax())
    data['GarageQual'] = data['GarageQual'].fillna(data['GarageQual'].value_counts().idxmax())
    data['GarageCond'] = data['GarageCond'].fillna(data['GarageCond'].value_counts().idxmax())
    data['PoolQC'] = data['PoolQC'].fillna("None")
    data['Fence'] = data['Fence'].fillna("None")
    data['MiscFeature'] = data['MiscFeature'].fillna("None")
    data['BsmtQual'] = data['BsmtQual'].fillna(data['BsmtQual'].value_counts().idxmax())
    data['BsmtCond'] = data['BsmtCond'].fillna(data['BsmtCond'].value_counts().idxmax())
    data['BsmtExposure'] = data['BsmtExposure'].fillna(data['BsmtExposure'].value_counts().idxmax())
    data['BsmtFinType1'] = data['BsmtFinType1'].fillna(data['BsmtFinType1'].value_counts().idxmax())
    data['BsmtFinType2'] = data['BsmtFinType2'].fillna(data['BsmtFinType2'].value_counts().idxmax())
    data['LotFrontage'] = data['LotFrontage'].fillna(data['LotFrontage'].mean())
    data['Electrical'] = data['Electrical'].fillna(data['Electrical'].value_counts().idxmax())
    data['MasVnrType'] = data['MasVnrType'].fillna(data['MasVnrType'].value_counts().idxmax())
    data['MasVnrArea'] = data['MasVnrArea'].fillna(data['MasVnrArea'].value_counts().idxmax())
    print(len(data))
    data.dropna(inplace=True)
    print(len(data))
    # data.dropna(inplace=True)
    # label_data = method.label_with_OE(data)
    # print(label_data.info())
    # y_data = data.pop("SalePrice")
    
    # data.drop(columns=['Alley', 'PoolQC', 'MiscFeature', 'Fence'], inplace=True)
    # plt.figure(figsize=(15,8))
    # sns.heatmap(data.isna(),cmap='Paired')
    # plt.show()
    # print(data.columns)

    # print(data.describe())
    # imputed_data = method.impute_col(data)
    # print(imputed_data.describe())
    # print(label_train_data)