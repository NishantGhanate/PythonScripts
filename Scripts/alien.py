# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:39:32 2019

@author: Nishant Ghanate
"""

# your code goes here
import pandas as pd

#Take User input for alphabetical order and string
#a= input('Enter the order of alphabet : \n')
#b= input('Enter the string you want to sort according to the Alphabet provided : \n')

a = "abcdefghijklmnopqrstuvwxyz"
b = "cyxbza"

df = []
#Combining both list to a new list
for i,j in zip(list(a),list(a.upper())):
    df.append(j)
    df.append(i)
#print(df)
a=df

#Converting list to the dataframe
alphabet = pd.DataFrame(index=range(0,len(a)),columns=['letter'])

spell = pd.DataFrame(index=range(0,len(b)),columns=['letter'])

alphabet['letter'] = list(a)
spell['letter'] = list(b)

#Sorting of String according to alphabet as per condition provided
alphabet=pd.merge(alphabet,spell,how='inner')

##Printing the final result
#output = ''.join(alphabet['letter'].values.tolist())
#print(output)