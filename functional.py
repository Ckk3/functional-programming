def search_obese(peoples_list=list()):
    obese = []
    if peoples_list['imc'] >= 30:
        obese.append(peoples_list)
    return obese

def get_all_imc(peoples_list=list()):
    new_imc_list = []
    for people in peoples_list:
        if people['imc'] >= 30:
            new_imc_list.append(int(people['imc']))
    return new_imc_list

peoples = [{'name': 'Joao', 'imc': 27},
         {'name': 'Cleiton', 'imc': 21},
         {'name': 'Julia', 'imc': 16},
         {'name': 'Carlos', 'imc': 43},
         {'name': 'Daniela', 'imc': 31}
]

#Using map()
names_list = list(map(lambda p: p['name'], peoples))
other_names_list = list(map(lambda p: p['name'], peoples))

print(f'names_list: {names_list}')
print(f'other_names_list: {other_names_list}')


#Using list()
people_with_obesity = list(filter(search_obese, peoples))
print(f'Peoples with obesity: {people_with_obesity}')

#Using reduce()
from functools import reduce
bmi_list = get_all_imc(peoples_list=peoples)
higher_bmi = reduce(lambda a,b : a if a > b else b,bmi_list)
print(f'Higher BMI: {higher_bmi}')