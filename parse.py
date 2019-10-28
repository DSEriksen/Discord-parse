import csv
import collections
import  xlsxwriter

authors = collections.Counter()

book = xlsxwriter.Workbook("ragnarokoutput.xlsx")
sheet = book.add_worksheet()
sRow = 0
sCol = 0

with open("ragnarok.csv", encoding="utf8") as input_file:
    for row in csv.reader(input_file, delimiter=";"):
        authors[row[1]] += 1

for name, value in authors.items():
    sheet.write(sRow, sCol, name)
    sheet.write(sRow, sCol + 1, value)
    sRow += 1

book.close()
print(authors)
