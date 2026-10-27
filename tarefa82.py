
print("Peça 11 números")
print("------------------------------")
print()

numeros = [0] * 11

for i in range(len(numeros)):
    numeros[i] = float(input("Me diga um número: "))

for i in range(len(numeros)):
    print(numeros[i])
    if i < len(numeros) - 1:
        print("--------------------------------------------")

