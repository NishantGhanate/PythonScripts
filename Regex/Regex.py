import re


strs = "how much for the maple syrup? $20.99? That's ricidulous!!!"
print (strs)
nstr = re.sub(r'[?|$|.|!]',r'',strs)
print (nstr)
nestr = re.sub(r'[^a-zA-Z0-9 ]',r'',nstr)
print (nestr)

