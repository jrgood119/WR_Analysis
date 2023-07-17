import pandas as pd

#class PreProcess:
"""This class takes an Excel input and converts it to a usuable format for analysis"""

def read_data():
    df = pd.read_excel('/Users/jtgood/Desktop/Python/WR_Model/WR_Edits.xlsx', index_col='Name')
    print(df.columns)
    df = df.drop(columns=['cfb_id','NFLfastR','PFF','PFR_ID'])
    print(df.columns)
    return df

print(read_data())