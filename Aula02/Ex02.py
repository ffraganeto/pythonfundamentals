# Coleções

dicionario = {
    'Morango': 3.50,
    'Banana': 2.20,
    'Melancia': 5.00,
}

dicionario['palavra'] # significado
    
    
exit()
# Definição da Variáveis
cesta = []
valores = [3.50, 2.20, 5.00]
soma = 0

# Processamento
while True:
    print('Escolha o seu produto:')
    
    produto = input('1- Morango, 2- Banana, 3- Melancia, 4- Sair')
    
    if produto == '1':
        cesta.append('Morango')
    elif produto == '2':
        cesta.append('Banana')
    elif produto == '3':
        cesta.append('Melancia')
    elif produto == '4':
        break
         
print(cesta)
for fruta in cesta:
    if fruta == 'Morango':
        soma += valores[0]
    elif fruta == 'Melancia':
        soma += valores[1]
    else:
        soma += valores[2]

#Saída        
print('O total da compra foi de :', soma)

exit()
#list()
            #0       #1   #2
lista = ['Fernando', 40, 'SP']
#primeiro elemento

print(lista[0])

### comportamentos

# inserção
lista.append('José')

# remover
lista.pop()

del lista[0]


exit()
# Estruturas de repetição
##FOR       # [0,11[
            # 0,1,2,3,4,5,6,7,8,9,10

lista = ['manga', 'banana', 'melancia']
for fruta in lista:
    print(fruta)

## Para cada numero no intervalo de 0-10
for numero in range(0,11):
    print(numero)

## numero = 0
## print(numero)

## numero = 1
## print(numero)

exit()
## WHILE
contagem = 0

while True:
    
    print('Escolha uma opcao:')
    
    if input('') == '1': 
        continue
    else:
        break
    
exit()
while contagem <= 10:
    print(contagem)
    contagem += 1
    
print('Sair do While')
