from docx import Document
import json
from docx.oxml import parse_xml
import tasks.task1

def generateDocument(inputFile="taskData.json", taskOutputFile="docx/tasks.docx", answerOutputFile="docx/answers.docx", variants=1, tasks=range(1,19)):
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
        task_number = 1

        # Здесь перебор по всем заданиям
        for task in tasks:
            current_task = task_data[str(task)]
            current_text = current_task['text'].split('/X/') if current_task['data'] is not None else str(task_number) + ") Данные задачи не найдены"
            current_data = current_task['data'][variant%len(current_task['data'])] if current_task['data'] is not None else []
            current_answer = current_task['answers'][variant%len(current_task['answers'])] if current_task['answers'] is not None else str(task_number) + ") Данные об ответе не найдены"
            variable_text = str(task_number)+") "
            if (len(current_data)>0):
                for i in range(len(current_data)):
                    variable_text += current_text[i]+current_data[i]
                variable_text += current_text[-1]
            else:
                variable_text = current_text

            task_document.add_paragraph(variable_text)
            answer_document.add_paragraph(current_answer)

            task_number += 1

        # Здесь конец перебора, добавление новой страницы для следующего варианта
        task_document.add_page_break()
        answer_document.add_page_break()

    task_document.save(taskOutputFile)
    answer_document.save(answerOutputFile)

def generateTask1():
    data = {}
    pass



generateDocument(variants=5, tasks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18])