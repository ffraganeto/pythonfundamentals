# Controle de Fluxo

# Criar uma calculadora em python
## Deverá realizar a soma, subtração, multiplicação e divisão
## O usuário deverá escolher a opção 1 - Soma, 2 - Sub, 3 - Mult, 4 - Div
## Opção Invalida

# 1. Capturar Números

opção = input('''
Escolha a opção matemática:
+ Para Soma
- Para subtração
* Para multiplicação
/ Para divisão
''')

number_1 = float(input('Informe o Primeiro Número: '))
number_2 = float(input('Informe o Segundo Número: '))

# 2. Realizar o Cálculo

# Adição
if opção == '+':
    print(int(number_1 + number_2))

# Subtração
elif opção == '-':
    print(int(number_1 - number_2))

# Multiplicação
elif opção == '*':
    print(int(number_1 * number_2))

# Divisão
elif opção == '/':
    print(int(number_1 / number_2))

else:
    print('Você digitou um operador não válido. Por favor repita a operação')

exit()
# Multiplas condições

## Crie um script em python que retorne o seu IMC

## IMC = PESO / ALTURA ** 2

### IMC  < 18.5 - Magreza
### 18.5 < IMC 24.9 - Normal
### 25 < IMC < 29,9 - Sobrepeso
### 30 < IMC < 39,9 - Obesidade
### IMC > 40 - Obesidade Grave

# 1. Capturar Peso e Altura
peso = float(input('Informe o seu peso:'))
altura = float(input('Informe a sua altura:'))

# 2. Calcular o IMC
imc = peso/(altura**2)
print(imc)

# 3. Comparar o IMC com as referências
if imc <= 18.5:
    # 4. Informar ao usuário a classificação
    print('IMC - Magreza')
elif imc < 24.9:
    print('IMC - Normal')
elif imc < 29.9:
    print('IMC - Sobrepeso')
elif imc < 39.9:
    print('IMC - Obesidade')
else:
    print('IMC - Obesidade Grave')



exit()
## > < != == >= <=

## 1. Capturar a idade
idade = int(input('Informe a sua idade'))

##2. Capturar a informação de Hab.
hab = input('Possui Habilitação? S/N:')

## 1. precisa ter idade >= 18
if idade >= 18 and hab.upper() == 'S':
    ## 2. precisa ter habilitação
    #if hab == 'S':
    print('Pode Dirigir')
else:
    print('Não Pode Dirigir')
