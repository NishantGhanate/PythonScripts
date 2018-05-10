from docx import Document

f = open('demo.docx','rb')
document = Document(f)
p = document.add_paragraph('B plain paragraph having some ')
document.save('demo2.docx')
f.close()