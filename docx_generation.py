from docx import Document
import json
from docx.oxml import parse_xml

def generateDocument(inputFile="taskData.json", taskOutputFile="docx/tasks.docx", answerOutputFile="docx/answers.docx", variants=1,):
    with open(inputFile, "r", encoding="utf-8") as file:
        task_data = json.load(file)

    task_document = Document()
    answer_document = Document()
    # p = document.add_paragraph('Вот пример формулы в OMML:')
    # omml_el = parse_xml(omml_formula)[0]
    # p._p.append(omml_el)

    for variant in range(variants):
        
        # Начало варианта
        task_document.add_heading("Вариант "+str(variant+1))
        answer_document.add_heading("Вариант "+str(variant+1))

        # Здесь перебор по всем заданиям
        task_number = 1
        current_task = task_data[str(task_number)]
        current_text = current_task['text'].split('/X/')
        current_data = current_task['data'][variant]
        current_answer = current_task['answers'][variant]
        variable_text = str(task_number)+") "
        for i in range(len(current_data)):
            variable_text += current_text[i]+current_data[i]
        variable_text += current_text[-1]
        task_document.add_paragraph(variable_text)
        answer_document.add_paragraph(str(task_number)+") "+current_answer)

        # Здесь конец перебора, добавление новой страницы для следующего варианта
        task_document.add_page_break()
        answer_document.add_page_break()

    task_document.save(taskOutputFile)
    answer_document.save(answerOutputFile)

generateDocument()