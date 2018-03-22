from .models import Anquan, Xianchang

import openpyxl

file = openpyxl.load_workbook("xianchang.xlsx")

sheet = file.get_sheet_by_name("简答题")

question = []
answer = []
for cell in sheet["C2":"C101"]:
    for cellobj in cell:
        question.append(cellobj.value)

for cell in sheet["H2":"H101"]:
    for cellobj in cell:
        answer.append(cellobj.value)


for i in range(len(question)):
    anquan = Xianchang.objects.create(question=question[i],answer=answer[i])
    anquan.save()