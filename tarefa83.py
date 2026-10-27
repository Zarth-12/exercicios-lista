
print("Me envie 18 numeros")
print("")

num = [0] * 18

for i in range(len(num)):
    num[i] = int(input("Me diga um numero: "))

print("Numeros na ordem inversa:")

for i in range(len(num) - 1, -1, -1):
    print(num[i])
