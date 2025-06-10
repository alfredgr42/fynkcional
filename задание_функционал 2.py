 import collections
pets = dict()

def pets_list(id):
    print("Ñïèñîê ïèòîìöåâ")
    print("---------------")
    for pet in pets:
        print(f'Èìÿ: {pets[id]['èìÿ']}, Âèä: {pets[id]["âèä"]}, Âîçðàñò: {suffix(pets[id]["âîçðàñò"])}')

def create():
    print('Ââåäèòå èíôîðìàöèþ î ïèòîìöå')
    name = input('Ââåäèòå èìÿ ïèòîìöà: ')
    species = input('Ââåäèòå âèä ïèòîìöà: ')
    age = int(input('Ââåäèòå âîçðàñò ïèòîìöà: '))
    owner_name = input('Ââåäèòå âëàäåëüöà ïèòîìöà: ')
    if pets:
        last_id = collections.deque(pets.keys(), maxlen=1)[0]
        new_id = last_id + 1
else:
    new_id = 1
    pets[new_id] = {'èìÿ': name, 'âèä': species, 'âîçðàñò': age, 'âëàäåëåö': owner_name}

def suffix(age):
    if 11 <= age % 100 <= 14:
        return f"{age} ëåò"
        elif age % 10 == 1:
            return f"{age} ãîä"
            elif age % 10 in [2, 3, 4]:
                return f"{age} ãîäà"
else:
    return f"{age} ëåò"

def delete(pet_id):
    if pet_id in pets:
        del pets[pet_id]
       print(f"Ïèòîìåö ñ èäåíòèôèêàòîðîì {pet_id} óäàëåí.")
else:
    print("Ïèòîìåö ñ òàêèì èäåíòèôèêàòîðîì íå íàéäåí.")

def update(pet_id, name=None, species=None, age=None):
    pet = pets.get(pet_id) if pet:
        if name:
            pet['name'] = name
            if species:
                pet['species'] = species
                if age is not None:
                    pet['age'] = age
                    print(f"Èíôîðìàöèÿ î ïèòîìöå ñ ID {pet_id} îáíîâëåíà.")
else:
    print(f"Ïèòîìåö ñ ID {pet_id} íå íàéäåí.")

def pets_id(pet_id):
    if pet_id in pets:
        print(pets[pet_id])
else:
    print(False)

while True:
    command = input("Ââåäèòå êîìàíäó (èëè 'stop' äëÿ âûõîäà) : ")
    if command.lower() == 'stop':
        print("Êîìàíäà 'stop' ïîëó÷åíà. Çàâåðøåíèå ïðîãðàììû.")
break
