import pandas as pd
import json

df = pd.read_json('ampl.json', lines = True)

print(df)
