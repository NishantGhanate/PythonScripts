import re 

lonPattern = "lat.*?"
latPattern  = "long.*?"

List = ['Latitude_A','Longitude_A' , 'Lat' , 'Long' , 'latitude' , 'longitude' , 'lattata' , 'longadada' ]

for word in List:
    if re.match(lonPattern , word.lower()):
        print(" pattern (lat.*?) Match =  "+ word )
    if re.match(latPattern , word.lower()):
        print(" pattern 1 (long.*?) Match =  "+ word)