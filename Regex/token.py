import re

token = '851568417:AAH3cOtvVaJ9RATU3cmW8l9BGu2VAHCpMBA'

a = re.findall('^[0-9]{9}:\w+',token)
print(a)
a = re.findall('^[0-9]{9}:[a-zA-Z0-9]{34}',token)
               
print(a)

a = re.search('^[0-9]{9}:[a-zA-Z0-9]{34}',token)            
print(a)

a = re.search('^[0-9]{9}:[a-z]{34}',token)              
print(a)
   
                
