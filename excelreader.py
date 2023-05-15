import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('File.xlsx', sheet_name='Sheet1')

list_of_Code = df['Row 3']
for i in list_of_Code.index:
    print(list_of_Code[i])
