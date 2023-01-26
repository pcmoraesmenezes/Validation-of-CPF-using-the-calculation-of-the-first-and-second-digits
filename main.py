"""
Verificador de cpf 
Calculo do primeiro digito ------
CPF: ___ ___ ___ -- __ 
Colete a soma dos 9 primeiros digitos multiplicando cada um pela contagem regressiva de 10, o primeiro digito deve ser multiplicado por 10, o segundo multiplicado por 9... e somar toda a multiplicação
Multiplicar a soma por 10
Pegar o resto da divisão por 11, se o resto for maior que 9, então o digito deverá ser 0, senao o digito devera ser o proprio numero
"""
import os
print("Bem vindo ao verificador de cpf! Para começarmos digite o cpf abaixo: ")
i = 0
calc = 0
contador = 0
cpf = input("")
print(f"O cpf digitado foi {cpf}")
while True:
    for j in cpf:
        if j == '-' or j == '.' or j == ' ':
            continue
        else:
            try:
                j == int(j)
                i = i + 1
            except:
                print("Você entrou com um caracter, insira apenas numeros inteiros! ")
                cpf = input()
                i = -1
                break        
    if i == 11:
        break
    elif i == -1: ##Quando o usuario digitar um caracter
        i = 0
        continue
    elif i == -2:
        print("Você digitou o CPF apenas com caracteres repetidos! Tente novamente ")
        cpf = input()
        continue
    else:
        i = 0 ##Quando o usuario digitar menos que 11 numeros
        print("Você não informou as quantidades de digitos necessários, lembre-se que o CPF é composto por 11 digitos inteiros! ")
        cpf = input()
repetidor = 10
for i in cpf:
    if i == '-' or i == '.' or i == ' ':
        continue
    else:
        calc = calc + (int(i) * repetidor)
        repetidor = repetidor - 1
        if repetidor == 1:
            break
calc = calc * 10
auxiliar = calc % 11
if auxiliar > 9:
    auxiliar = 0
else:
    auxiliar = calc % 11
os.system('cls' if os.name == 'nt' else 'clear')
print(f'O primeiro digito é: {auxiliar}')
"""
--------- Calculo do segundo digito do cpf -----------
Incluir o primeiro digito na soma
"""
calc = 0
repetidor = 11
for i in cpf:
    if i == '-' or i == '.' or i == ' ':
        continue
    else:
        calc = calc + (int(i) * repetidor)
        repetidor = repetidor - 1
        if repetidor == 2:
            break
segundo_digito = calc + (auxiliar * 2)
segundo_digito = segundo_digito * 10
if segundo_digito % 11 > 9:
    segundo_digito = 0
else:
    segundo_digito = segundo_digito % 11
print(f'O segundo digito é: {segundo_digito}')
if str(auxiliar) == cpf[9] and str(segundo_digito) == cpf[10]:
    print("Parabéns, você informou um CPF válido!")
else:
    print("Desculpe, mas o CPF informado é inválido.")