import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "name": ["pranav", "ayush" , "anuj" , "devansh" , "indore"],
    "age": [25, np.nan, 23, 29, np.nan],
    "score": [85, 69, np.nan, 92, 88],
    }
df = pd.DataFrame(data)
file_path = "abd.csv"
df.to_csv(file_path,index=False)
print(df)
