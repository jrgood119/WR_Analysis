import pandas as pd

class PreProcess:
    """This class takes an Excel input and converts it to a usuable format for analysis"""

    def __init__(self):
        self.raw_df = pd.read_excel('WR_Edits.xlsx')

        return raw_df
    

if __name__ == '__main__':
    print(PreProcess)