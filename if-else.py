# IF-ELSE 
print('\n+++++++++++++++++ IF-ELSE +++++++++++++++++\n')
# Ejemplo 1
print('============ Ejemplo 1 ============')
condicion1 = True
if condicion1 == True:
    print('La condicion es verdadera')
else:
    print('La condicion es falsa')
    
    
# Ejemplo 2
print('============ Ejemplo 2 ============')
efectivo = False
tarjeta_credito = True
if efectivo == True:
    print('Puedes pagar tus gastos pagando en efectivo')
elif tarjeta_credito == True:
    print('Puedes pagar tus gastos pagando con tu tarjeta de credito')
else:
    print('Lo siento, no tienes como pagar tus gastos')
    
    
# Ejemplo 3
print('============ Ejemplo 3 ============')
numero1 = 10
numero2 = 10
if numero1 > numero2:
    print(f'{numero1} es mayor que {numero2}')
elif numero1 < numero2:
    print(f'{numero1} es menor que {numero2}')
else:
    print(f'{numero1} y {numero2} son iguales')
    

# OPerador Ternario
print('\n+++++++++++++++++ Ternary Operator +++++++++++++++++\n')
# Ejemplo 1
print('============ Ejemplo 1 ============')
sesion_iniciada = True
print('Sesion Iniciada, Bienvenido!') if sesion_iniciada == True else print('No tienes sesion iniciada')


# Ejemplo 2
print('============ Ejemplo 2 ============')
edad = 18
print('Eres mayor de edad, ahora puedes votar') if edad >= 18 else print('Aun eres menor de edad, no puedes votar')


# Ejemplo 3
print('============ Ejemplo 3 ============')
puerta_abierta = False
print('La puerta esta abierta') if puerta_abierta == True else print('La puerta esta cerrada')