from docx import Document

#ReadBinary mode
f = open('demo.docx','rb')
document = Document(f)
#append file
p = document.add_paragraph('B plain paragraph having some ')
document.save('demo2.docx')
f.close()