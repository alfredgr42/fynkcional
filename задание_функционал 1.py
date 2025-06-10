def factorial(n):
    if n == 0 or n == 1:
        return 1
else:
    return n * factorial(n - 1)
def factorials_list(n):
    fact_n = factorial(n)
    print(f"Ôàêòîðèàë ÷èñëà {n} ðàâåí: {fact_n}")
    factorials = []
    for i in range(fact_n, 0, -1):
        factorials.append(factorial(i))
        return factorials
        number = int(input('Ââåäèòå ÷èñëî: '))
        result = factorials_list(number)
        print("Ñïèñîê ôàêòîðèàëîâ îò", factorial(number), "äî 1:", result)
