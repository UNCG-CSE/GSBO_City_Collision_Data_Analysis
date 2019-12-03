import pandas as pd
import numpy as np
import re
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori 
from mlxtend.frequent_patterns import association_rules

data = pd.read_csv(r"C:\Users\sahit\OneDrive\Documents\1Gradproject\NEW\Transactions.txt",sep='\t',header=None)
data1 = pd.DataFrame(data[0].str.split(",",n=1,expand=True))
data1= data1.replace(np.nan, '', regex=True)
data2=[]
for x,y in data1.itertuples(index=False):
    data2.append(re.findall('(GO:.*?)\,',y))
    for i in range(0,len(data2)):
    data2[i].insert(0, data1[0][i])
    