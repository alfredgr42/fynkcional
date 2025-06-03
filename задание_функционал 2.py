 import collections
pets = dict()

def pets_list(id):
print("������ ��������")
print("---------------")
for pet in pets:
print(f'���: {pets[id]['���']}, ���: {pets[id]["���"]}, �������: {suffix(pets[id]["�������"])}')

def create():
print('������� ���������� � �������')
name = input('������� ��� �������: ')
species = input('������� ��� �������: ')
age = int(input('������� ������� �������: '))
owner_name = input('������� ��������� �������: ')
if pets:
last_id = collections.deque(pets.keys(), maxlen=1)[0]
new_id = last_id + 1
else:
new_id = 1
pets[new_id] = {'���': name, '���': species, '�������': age, '��������': owner_name}

def suffix(age):
if 11 <= age % 100 <= 14:
return f"{age} ���"
elif age % 10 == 1:
return f"{age} ���"
elif age % 10 in [2, 3, 4]:
return f"{age} ����"
else:
return f"{age} ���"

def delete(pet_id):
if pet_id in pets:
del pets[pet_id]
print(f"������� � ��������������� {pet_id} ������.")
else:
print("������� � ����� ��������������� �� ������.")

def update(pet_id, name=None, species=None, age=None):
pet = pets.get(pet_id) if pet:
if name:
pet['name'] = name
if species:
pet['species'] = species
if age is not None:
pet['age'] = age
print(f"���������� � ������� � ID {pet_id} ���������.")
else:
print(f"������� � ID {pet_id} �� ������.")

def pets_id(pet_id):
if pet_id in pets:
print(pets[pet_id])
else:
print(False)

while True:
command = input("������� ������� (��� 'stop' ��� ������) : ")
if command.lower() == 'stop':
print("������� 'stop' ��������. ���������� ���������.")
break