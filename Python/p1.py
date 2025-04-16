import pandas as pd
import os
a=os.listdir("C:/Users/607-12/ppp/")
p=[]
for i in a:
    p.append(pd.read_csv(f"C:/Users/607-12/ppp/{i}"))
print(p)