import pandas as pd
import json
a = pd.DataFrame(json.loads(open('data.json','r+').read()))
print(a.head())          
a.to_csv('data.csv')
