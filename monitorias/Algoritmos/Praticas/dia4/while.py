# pegar um numero e pegar os digitos dele

num = int(input("Digite um número:\n--> "))

lista = []

while (num > 0):
    unidade = num % 10
    num = num // 10
    lista.append(unidade)








for numero in lista:
    print(numero)
