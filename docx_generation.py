from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('Вариант 1', 0)

p = document.add_paragraph('ФыафаФыафаыФЫАФ ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.save('demo.docx')