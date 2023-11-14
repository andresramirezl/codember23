"""
"#" Aumenta el valor numérico en 1.
"@" Disminuye el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual.
El valor numérico inicial es 0 y las operaciones deben aplicarse en el orden en que aparecen en la cadena de símbolos.

"""

def contar_palabras(ruta_archivo):
    
    with open('message_01.txt', 'r') as archivo:
        contenido = archivo.read()
        
        
    palabras = contenido.split()
    frecuencia_palabras = {}

    for palabra in palabras:
        palabra = palabra.lower()
        
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
            
        else:
            frecuencia_palabras[palabra] = 1

    resultado = ''.join([f'{palabra}{frecuencia}' for palabra, frecuencia in frecuencia_palabras.items()])
    
    print(resultado)        
            
ruta_del_archivo = 'message_01.txt'

contar_palabras(ruta_del_archivo)