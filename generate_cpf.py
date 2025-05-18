import random

resposta = input("Deseja gerar um novo CPF? (sim/não): ").strip().lower()

if resposta == "sim":
    def gerar_cpf(qtd, minimo=0, maximo=9):
    
    #Gera os números aleatório
        CPFs_gerados = [random.randint(minimo, maximo) for _ in range(qtd)]

        # Primeiro dígito verificador
        soma1 = sum([CPFs_gerados[i] * (10 - i) for i in range(9)])
        digito1 = 0 if soma1 % 11 < 2 else 11 - (soma1 % 11)

        CPFs_gerados.append(digito1)

        # Segundo Número
        soma2 = sum([CPFs_gerados[i] * (11 - i) for i in range(10)])
        digito2 = 0 if soma2 % 11 < 2 else 11 - (soma2 % 11)

        CPFs_gerados.append(digito2)

        CPF = ''.join(map(str, CPFs_gerados))
        return CPF

    cpf_gerado = gerar_cpf(9)
    cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"
    print("O CPF gerado foi:", cpf_formatado)

elif resposta == "não" or resposta == "nao":
    print("Você escolheu NÃO. programa va ser fechado.")
    exit()
else:
    print("Resposta inválida. Digite apenas 'sim' ou 'não'.")
    exit()
