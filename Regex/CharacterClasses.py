import re

pattern = "[A-Z]"

if re.search(pattern , "This is python look "):
    print("Match 1")

if re.search(pattern , "THIS IS PYTHON LOOK "):
    print("Match 2")

if re.search(pattern , "This Is Python LooK 12 "):
    print("Match 3")
