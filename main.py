from queue import PriorityQueue


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

def contadordigitos(n1):
    if n1 < 10:
        return 1
    else:
        return 1+ contadordigitos(n1/10)



print("menu")
seleccion = ""
while seleccion != "0":
    print("1. Invertir")
    print("2. Sumar")
    print("3. Cuenta Regresiva")
    print("4. Contador")
    seleccion=int(input())

    if seleccion == "1":
        texto=input("Ingrese el texto: ")
        print("Invertir")

    elif seleccion == "2":
        n = int(input("Ingrese el numero: "))
        print("Sumar")

    elif seleccion == "3":
        numero = int(input("Ingrese el numero: "))
        print("Cuenta Regresiva")

    elif seleccion == "4":
        n1=input(input("Ingrese el numero: "))
        print(contadordigitos(n1))

    elif seleccion == "0":
        print("Programa terminado")

