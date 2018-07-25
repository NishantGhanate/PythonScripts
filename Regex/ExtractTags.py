import re
import os
from pandas import read_csv

scriptDir = os.path.dirname(os.path.realpath(__file__))
tags = list()

# . means staring with and ? means end with 
# start with < and end with >
pattern = "<.*?>"

csvfile = read_csv(scriptDir + os.path.sep +'Book1.csv')

# : all values on 1 index  
lines = csvfile.iloc[:, 1].values 
print(lines)

for line in lines:
    result = re.search(pattern,line)
    if result:
        tags.append(result.group())
 
f = open(scriptDir + os.path.sep +'tags.txt','a+')
myset = set(tags)
for tag in myset:
    print(tag)
    f.write(tag + '\n')

f.close()
        