import random
import math
from scipy.stats import laplace
from scipy.special import erf

def generate_task10(task_doc, answer_doc, task_number):

    a = random.randint(1, 9)/10
    b = random.randint(25, 75)*2
    c = random.randint(20, 40)

    task_text = f"Вероятность выхода из строя за время Т одного конденсатора равна {a}. Определить вероятность того, что за время Т из {b} конденсаторов, работающих независимо, выйдут из строя:\nа) не менее {c} конденсаторов;\nб) ровно половина."

    Phi = lambda x: erf((x/2**0.5)/2)
    a_answer = Phi(b)-Phi(c)
    b_answer = (1/math.sqrt(2*3.14)) * math.exp((-(b//2)**2)/2)

    task_answer = f"а){a_answer}; б){b_answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")