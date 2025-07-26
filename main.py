
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

def contadordigitos(dato):
    dato = (dato)
    if dato < 10:
        return 1
    else:
        return 1 + contadordigitos(dato // 10)



dato = int(input("Ingresa un numero: "))
print(contadordigitos(dato))





