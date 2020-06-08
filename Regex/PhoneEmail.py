import re 


text = 'They see me rolling something@email.com they +918453246748'
emails = ''
phones = ''
if text:
    emails = re.findall('\S+@\S+', text)
    phones = re.findall('\\+?(?:\\s*?\\d{3,15}\\-*?)+',text)

print(emails,phones)

