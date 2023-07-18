import pandas as pd

class PreProcess:
    """This class takes an Excel input and converts it to a usuable format for analysis"""

    def __init__(self):
        pass

    def read_data():
        """This functions reads in excel data to be used and drops unwanted columns"""
        df = pd.read_excel('/Users/jtgood/Desktop/Python/WR_Model/WR_Edits.xlsx', index_col='Name')
        print(df.columns)
        df = df.drop(columns=['cfb_id','NFLfastR','PFF','PFR_ID'])
        print(df.columns)
        return df
    
    def remove_nulls(df):
        """This function will remove nulls from the data"""


    def set_types():
        """This functions converts data types to usable formats"""


print(PreProcess.read_data())