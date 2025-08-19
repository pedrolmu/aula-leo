import json
#substitua seuqrquivo.json pelo nome de seu arquivo json

with open('seuarquivo.jason', 'r', encoding='utf-8') as jsonfile:
    data= json.load(jsonfile)
    print(data)