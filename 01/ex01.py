from random import randint


numeros = []

for i in range(100):
    numeros.append(randint(1000))

maior = -1
count_pares = 0
count_menor_100 = 0

for n in numeros:
    if n > maior:
        maior = n

    if n % 2 == 0:
        count_pares += 1

    if n < 100:
        count_menor_100 += 1

print(f"O maior número gerado foi {maior}")
print(f"Foram gerados {count_pares} numeros pares")
print(f"Foram gerados {count_menor_100} numeros menores que 100")
