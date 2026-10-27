
print("Algoritmo de numeros pares e impares")
print()

n = [0] * 12

for i in range(len(n)):
    n[i] = int(input("Me diga um numero: "))

print("Numeros pares")

for i in range(len(n)):
    if n[i] % 2 == 0:
        print(n[i])

print("Numeros impares")

for i in range(len(n)):
    if n[i] % 2 != 0:
        print(n[i])
