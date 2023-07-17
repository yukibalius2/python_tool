import pandas as pd
import sys
args = sys.argv

data = pd.read_excel(args[0])
data.to_csv('csv_data.csv',encoding='utf-8')
