import pandas as pd

if __name__ == "__main__":
    train_data = pd.read_csv("dataSets/train.csv")
    print(train_data.describe())
    print(train_data.isnull().sum())
    print(train_data.columns)
