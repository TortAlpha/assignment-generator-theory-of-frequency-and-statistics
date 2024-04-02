from docx import Document
from docx.oxml.ns import qn

from docx.oxml import parse_xml


# Пример OMML формулы (здесь должен быть ваш OMML код)
omml_formula = """
<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSup>
      <m:e>
        <m:r>
          <m:t>x</m:t>
        </m:r>
      </m:e>
      <m:sup>
        <m:r>
          <m:t>2</m:t>
        </m:r>
      </m:sup>
    </m:sSup>
  </m:oMath>
</m:oMathPara>
"""

document = Document()
p = document.add_paragraph('Вот пример формулы в OMML:')
omml_el = parse_xml(omml_formula)[0]
p._p.append(omml_el)

document.save('omml_formula.docx')
