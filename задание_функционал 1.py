def factorial(n):
if n == 0 or n == 1:
return 1
else:
return n * factorial(n - 1)

def factorials_list(n):
fact_n = factorial(n)
print(f"��������� ����� {n} �����: {fact_n}")
factorials = []
for i in range(fact_n, 0, -1):
factorials.append(factorial(i))
return factorials

number = int(input('������� �����: '))
result = factorials_list(number)
print("������ ����������� ��", factorial(number), "�� 1:", result)