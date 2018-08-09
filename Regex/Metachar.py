import re

pattern = "gr.y"

# start with gr and y end with 
pattern1 = "gr.*?y"

List =  ["grey" , "gray" , "groy" , "greey"]

for word in List:
    if re.match(pattern , word):
        print(" pattern (gr.y) Match =  "+ word )
    if re.match(pattern1 , word):
        print(" pattern 1 (gr.*?y) Match =  "+ word )
    

