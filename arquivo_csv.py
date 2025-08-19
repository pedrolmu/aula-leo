import csv

# substitua 'seuarquivo.csv' pelo nome do seu arquivo csv
with open('seuarquivo.csv', newline='', encoding='utf-8')as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)   