# functions I have to use: .map .filter .reduce
# Datas: Name, Age, imc, height, mass.
# filter: See the imc average
# map: Put names in Upper
# replace: blah

# Imperative Programming
def upper_name(names_list=list()):
    new_list = []
    for name in names_list:
        new_list.append(name.upper())

    return new_list

def get_names(peoples_list=list()):
    for people in peoples_list:
        names.append(people['name'])


peoples = [{'name': 'Joao', 'imc': 27},
         {'name': 'Cleiton', 'imc': 21},
         {'name': 'Julia', 'imc': 16},
         {'name': 'Carlos', 'imc': 43},
         {'name': 'Daniela', 'imc': 31}
]
names = []
uppered_names = []

# for item in peoples:
# uppered_names.append(item['name'].upper())


get_names(peoples)
print(names)
get_names(peoples)
print(names)



