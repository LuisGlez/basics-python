# For loop 
print('\n+++++++++++++++++ For loop +++++++++++++++++\n')
# Ejemplo 1
print('============ Ejemplo 1 ============')
lenguajes_programacion = ['JavaScript', 'Python', 'C++', 'Java']
for lenguaje in lenguajes_programacion:
    print(lenguaje)
    

# Ejemplo 2
print('============ Ejemplo 2 ============')
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for numero in numeros:
    print(numero)
    
    
# Ejemplo 3
print('============ Ejemplo 3 ============')
numeros_pares = []
numeros_impares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
        

print(f'Los numeros pares son:\n{numeros_pares}')
print(f'Los numeros impares son:\n{numeros_impares}')


# While
print('\n+++++++++++++++++ While +++++++++++++++++\n')
# Ejemplo 1
print('============ Ejemplo 1 ============')
iterador = 0
while iterador <= 10:
    print(iterador)
    iterador += 1


# Ejemplo 2
print('============ Ejemplo 2 ============')
numero = int(input('Introduce un numero: (0 para finalizar)'))
while numero != 0:
    print(f'Haz introducido el numero {numero}')
    numero = int(input('Introduce un numero: (0 para finalizar)'))
    

# Ejemplo 3
print('============ Ejemplo 3 ============')
contador = 0
while contador < 3:
    print('Saludos desde bucle While')
    contador += 1