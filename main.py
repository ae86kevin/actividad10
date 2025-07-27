
def invertirtexto(texto):
    if texto == "":
        return 0
    else:

        return texto[::-1]

def sumar(n):
    if n == 0:
        return 0
    else:
        return n + sumar(n-1)


def cuentaregresiva(numero):
    if numero == 0:
        return 0
    else:
        print(numero)
        cuentaregresiva(numero - 1)

def contadordigitos(n):
    if n < 10:
        return 1
    else:
        return 1+ contadordigitos(n/10)

n= int(input("Ingresa un numero: "))
print(f"EL numero ingresado tiene la cantidad de digitos: {contadordigitos(n)}")




