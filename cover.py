import docx
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


def collect_data():
    problems = []
    set_number = eval(input("Enter Problem Set Number \n"))
    while True:
        temp = input("Enter Problem Titles, !q to quit \n")
        if not temp == "!q":
            problems.append(temp)
        else:
            break
    generate(problems, set_number)


def generate(problems, set_number):
    document = docx.Document()
    paragraph = document.add_paragraph("Wesley Turner")
    center(paragraph)
    paragraph = document.add_paragraph("CM 1295")
    center(paragraph)
    paragraph = document.add_paragraph("AC Circuits")
    center(paragraph)
    paragraph = document.add_paragraph("ECE 204-03")
    center(paragraph)
    set_number = "HW # " + str(set_number)
    paragraph = document.add_paragraph(set_number)
    center(paragraph)
    for k in range(10):
        document.add_paragraph()
    for k in range(len(problems)):
        problem_number = str(problems[k]) + '__________'
        paragraph = document.add_paragraph(problem_number)
        center(paragraph)
    document.save('Cover_Page.docx')


def center(paragraph):
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER


if __name__ == "__main__":
    collect_data()
