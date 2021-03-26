def get_names(peoples_list):
    for people in peoples_list:
        names_list.append(people['name'])
    return names_list

def search_obeses_imperative(peoples_list):
    for people in peoples_list:
        if people['imc'] >= 30:
            obeses_list.append(people)
    return obeses_list

peoples = [{'name': 'Joao', 'imc': 27},
         {'name': 'Cleiton', 'imc': 21},
         {'name': 'Julia', 'imc': 16},
         {'name': 'Carlos', 'imc': 43},
         {'name': 'Daniela', 'imc': 31}
]

names_list = []
names_list = get_names(peoples_list=peoples)
other_names_list = get_names(peoples_list=peoples)

print(f'Names: {names_list}')
print(f'Other names: {other_names_list}')

obeses_list = []
obeses_list = search_obeses_imperative(peoples_list=peoples)
print(f'Obeses: {obeses_list}')