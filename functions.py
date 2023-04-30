# Functions 
print('\n+++++++++++++++++ Functions +++++++++++++++++\n')
# Ejemplo 1
print('============ Ejemplo 1 ============')
def saludar():
    print('Hola desde una funcion')
    

saludar()


# Ejemplo 2
print('============ Ejemplo 2 ============')
def sumar(numero1, numero2):
    return numero1 + numero2


print(f'El resultado de la suma es: {sumar(7, 4)}')


# Ejemplo 3
print('============ Ejemplo 3 ============')
contador = 0

def incrementar_contador(contador):
    return contador + 1
    

def mostrar_contador(contador):
    print(f'Se ha llamado a la funcion \'incrementar_contador\' un total de: {contador} veces')
    
    
contador = incrementar_contador(contador)
contador = incrementar_contador(contador)
contador = incrementar_contador(contador)

mostrar_contador(contador)

# Default Parameters 
print('\n+++++++++++++++++ Default Parameters +++++++++++++++++\n')
# Ejemplo 1
print('============ Ejemplo 1 ============')
def suma(num1 = 0, num2 = 0):
    return num1 + num2


print(f'funcion suma {suma(8, 3)}')
print(f'funcion suma {suma(2)}')


# Ejemplo 2
print('============ Ejemplo 2 ============')
def llenar_informacion(nombre, edad, telefono = 'S/N', correo = 'S/N'):
    informacion_personal = {
        'Nombre': nombre,
        'Edad': edad,
        'Telefono': telefono,
        'Correo': correo
    }
    return informacion_personal
    

informacion_personal = llenar_informacion('Pedro', 40)
print(informacion_personal)


# Ejemplo 3
print('============ Ejemplo 3 ============')
def saludo(nombre = 'Sr o Sra'):
    print(f'Bienvenido {nombre}')
    

saludo('Juan')
saludo()



# Keyword Arguments 
print('\n+++++++++++++++++ Keyword Arguments +++++++++++++++++\n')
# Ejemplo 1
print('============ Ejemplo 1 ============')
def potencia(base, exponente):
    return base ** exponente


print(f'{potencia(exponente = 3, base = 2)}')


# Ejemplo 2
print('============ Ejemplo 2 ============')
def nombres(primer_nombre, segundo_nombre):
    print(f'Hola, {primer_nombre} {segundo_nombre}')
    

nombres(segundo_nombre='Angel', primer_nombre='Luis')


# Ejemplo 3
print('============ Ejemplo 3 ============')
def division(dividendo, divisor):
    return dividendo / divisor


print(f'El resultado de la division en: {division(divisor=2, dividendo=24)}')