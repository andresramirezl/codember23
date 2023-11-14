"""
    "#" Increases the numeric value by 1.
    "@" Decreases the numeric value by 1.
    "*" Multiplies the numeric value by itself.
    "&" Prints the current numeric value.
    The initial numeric value is 0 and the operations should be applied in the order in which they appear in the string of symbols.

"""


with open('message_02.txt', 'r') as archivo:
        contenido = archivo.read()
              
palabras = list(contenido)
valor = 0
valor_list = []

for palabra in palabras:
    if palabra == '#':
        valor = valor + 1
    elif palabra == '@':
        valor = valor - 1 
    elif palabra == '*':
        valor = valor * valor
    else:
        valor_list.append(valor)
      
print(''.join(map(str, valor_list)))


    
