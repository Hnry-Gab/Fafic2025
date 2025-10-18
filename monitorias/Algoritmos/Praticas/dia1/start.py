# CRIAR VARIAVEIS
print("\n"*100)
numero = int(input("Digite o número: \n"))
centenas_string = ""
dezenas_string = ""
unidades_string = ""

# PEGAR OS VALORES, A UNIDADE, A DEZENA E A CENTENA
unidades = numero % 10
numero = numero // 10
dezenas = numero % 10
numero = numero // 10
centenas = numero % 10

# CRIAR A PALAVRA QUE FALA QUANTAS DE CADA TEM
if centenas > 0:
    if centenas > 1:
        centenas_string = f"{centenas} Centenas"
    else:
        centenas_string = f"{centenas} Centena"
if dezenas > 0:
    if dezenas > 1:
        dezenas_string = f"{dezenas} Dezenas"
    else:
        dezenas_string = f"{dezenas} Dezena"
if unidades > 0:
    if unidades > 1:
        unidades_string = f"{unidades} Unidades"
    else:
        unidades_string = f"{unidades} Unidade"

# VERIFICAR OS CASOS PARA VER COMO PRINTAR NO TERMINAL
if centenas_string != "" and dezenas_string != "" and unidades_string != "":
    # Existe os 3
    print(f"{centenas_string}, {dezenas_string} e {unidades_string}")

elif centenas_string != "" and dezenas_string != "" and unidades_string == "":
    # Existe Centena e Dezena
    print(f"{centenas_string} e  {dezenas_string}")

elif centenas_string != "" and unidades_string != "" and dezenas_string == "":
    # Existe Centena e Unidade
    print(f"{centenas_string} e {unidades_string}")

elif centenas_string != "" and unidades_string == "" and dezenas_string == "":
    # Existe Centena
    print(f"{centenas_string}")

elif dezenas_string != "" and unidades_string != "":
    # Dezenas e Unidades
    print(f"{dezenas_string}  e  {unidades_string}")

elif dezenas_string != "" and unidades_string == "":
    # Dezenas 
    print(f"{dezenas_string}")

elif unidades_string != "":
    # Unidades
    print(f"{unidades_string}")