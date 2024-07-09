import pandas as pd

def merge_dataset(df1, df2, key):
    # Merge two datasets
    # df1: DataFrame 1
    # df2: DataFrame 2
    # key: column to merge on
    # return: merged DataFrame
    return pd.merge(df1, df2, on=key)