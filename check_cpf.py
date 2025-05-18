cpf = input("Digite o CPF que deseja verificar: ")

if not cpf.isdigit() or len(cpf) != 11:
    print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")

else:
    numeros = [int(d) for d in cpf]

    # Primeiro dígito verificador
    soma1 = sum([numeros[i] * (10 - i) for i in range(9)])
    digito1 = 0 if soma1 % 11 < 2 else 11 - (soma1 % 11)

    # Segundo Número
    soma2 = sum([numeros[i] * (11 - i) for i in range(10)])
    digito2 = 0 if soma2 % 11 < 2 else 11 - (soma2 % 11)

    #Formatar CPF
    CPF_Formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    #Verificando o 10° e o 11° número
    if numeros[9] == digito1 and numeros[10] == digito2:
        print(f"O CPF {cpf} é Válido")

    else:
        print(f"O CPF {cpf} é Inválido")