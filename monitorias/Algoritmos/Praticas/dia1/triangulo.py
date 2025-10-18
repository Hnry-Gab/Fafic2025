lado1 = int(input())
lado2 = int(input())
lado3 = int(input())


if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Escaleno")
elif lado1 == lado2 and lado2 == lado3:
    print("Equilátero")
else:
    print("s")

