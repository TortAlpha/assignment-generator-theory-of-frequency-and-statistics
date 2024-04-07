from docx import Document
from docx.oxml import parse_xml

document = Document()
p = document.add_paragraph('Вот пример формулы в OMML:')
omml_el = parse_xml(omml_formula)[0]
p._p.append(omml_el)

document.save('omml_formula.docx')
