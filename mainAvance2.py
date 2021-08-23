import sys
import pandas as pd
from tabulate import tabulate

# menu
def menuBienvenida():
    print("\n\tHola, Bienvenido a la Calculadora de Tablas de Verdad!")
    print(
        "Instrucciones para usar la calculadora: \n1. Solo puedes usar las proposiciones p, q, r, s, t \n2. Indicar jerarquía de operaciones con paréntesis\n")
    print(
        "Operadores por Jerarquía\nNegación: ~ (alt+126) \nConjunción: ^ (alt+94)\nDisyunción: v (letra)\nCondicional: → (copiar y pegar)\nBicondicional: ↔ (copiar y pegar)")


def numPremisa():
    while True:
        try:
            n = int(input("\n¿Cuántas premisas tendra tu argumento? (La conclusión no cuenta): "))
            if (n <= 4 and n > 0):
                break
            else:
                print("El programa solo admite hasta 4 premisas.")
        except ValueError:
            print("Porfavor introduce un dato válido.")
    return n


def introPremisas(n):
    p = []

    for i in range(n + 1):
        if (i == n):
            # po = input("Introduce la conclusión: ")
            print("Introduce la conclusión: ")
            po = input()

        else:
            # po = input("Introduce la premisa número", i + 1, ": ")
            print("Introduce la premisa número", i + 1, ": ")
            po = input()

        p.append(po.replace(" ", ""))
    # print(p)
    return p


def numprop(p):
    simbolos = ["~", "^", "v", "→", "↔", "(", ")"]
    strp = "".join(p)
    # print(strp)
    pr = list(strp)
    pr = [q for q in pr if q not in simbolos]  # enunciado sin símbolos
    return len(set(pr)), pr  # regresa el número de letras (p q r s t)


def renglones(n, pr):
    renglon = 2 ** n  # número de renglones
    tabla = []
    pr = list(set(pr))
    # print(pr)
    for i in range(n):
        tabla.append(pr[i:i + 1])
        # print("\n")
    # print(tabla)
    p = n
    for i in range(n):
        p = p - 1
        iteracion = 2 ** p
        while renglon > 0:
            for j in range(iteracion):
                tabla[i].append(True)
                renglon -= 1
            for j in range(iteracion):
                tabla[i].append(False)
                renglon -= 1
        renglon = 2 ** n
    # print(tabla)
    return tabla


def operaciones(p, n, tabla):
    strp = "".join(p)  # junta premisas en string
    k = 0  # contador para escoger el caracter
    for i in strp:
        # print(i,k)
        if i == '~':
            a = strp[k + 1]  # letra que se va a negar
            # print(a)
            negacion(tabla, a, n)
        elif i == '^':
            a, b = strp[k - 1], strp[k + 1]
            conjuncion(tabla, a, b, n)
        elif i == 'v':
            a, b = strp[k - 1], strp[k + 1]
            disyuncion(tabla, a, b, n)
        elif i == '→':
            a, b = strp[k - 1], strp[k + 1]
            condicional(tabla, a, b, n)
        elif i == '↔':
            a, b = strp[k - 1], strp[k + 1]
            bicondicional(tabla, a, b, n)
        k += 1


def negacion(tabla, a, n):  # a=proposición a negar n=número total de proposiciones
    newcolumn = []
    for i in range(n):
        if a == tabla[i][0]:  # proposición que va a ser negado
            newcolumn.append('~' + a)  # titulo de la columna
            for j in range(1, 2 ** n + 1):
                value = not (tabla[i][j])  # negación de la columna seleccionada
                newcolumn.append(value)
    tabla.append(newcolumn)


def conjuncion(tabla, a, b, n):  # a primer proposicion y b segunda proposicion
    newcolumn = []
    for i in range(n):
        for j in range(n):
            if a == tabla[i][0] and b == tabla[j][0]:  # proposiciones que se usaran
                newcolumn.append(a + '^' + b)  # titulo de la columna
                for k in range(1, 2 ** n + 1):
                    value = tabla[i][k] and tabla[j][k]  # operador logico
                    newcolumn.append(value)
    tabla.append(newcolumn)


def disyuncion(tabla, a, b, n):  # a primer proposicion y b segunda proposicion
    newcolumn = []
    for i in range(n):
        for j in range(n):
            if a == tabla[i][0] and b == tabla[j][0]:  # proposiciones que se usaran
                newcolumn.append(a + 'v' + b)  # titulo de la columna
                for k in range(1, 2 ** n + 1):
                    value = tabla[i][k] or tabla[j][k]  # operador logico
                    newcolumn.append(value)
    tabla.append(newcolumn)


def condicional(tabla, a, b, n):  # a primer proposicion y b segunda proposicion
    newcolumn = []
    for i in range(n):
        for j in range(n):
            if a == tabla[i][0] and b == tabla[j][0]:  # proposiciones que se usaran
                newcolumn.append(a + '→' + b)  # titulo de la columna
                for k in range(1, 2 ** n + 1):
                    if tabla[i][k] == True and tabla[j][k] == False:  # condiciones
                        value = False
                    else:
                        value = True
                    newcolumn.append(value)
    tabla.append(newcolumn)


def bicondicional(tabla, a, b, n):
    newcolumn = []
    for i in range(n):
        for j in range(n):
            if a == tabla[i][0] and b == tabla[j][0]:  # proposiciones que se usaran
                newcolumn.append(a + '↔' + b)  # titulo de la columna
                for k in range(1, 2 ** n + 1):
                    if tabla[i][k] == tabla[j][k]:  # condiciones
                        value = True
                    else:
                        value = False
                    newcolumn.append(value)
    tabla.append(newcolumn)

    '''
# p=['premisa1','premisa2','conclusión']


def generar_tabla(tablar):
   
    d = {'premisas': pd.Series(tablar)}
    print(pd.DataFrame(d))
    df = pd.DataFrame(d)
    print(df.iloc[0])
    #print(df.melt(id_vars=[tablar], var_name=p, value_name=p))
'''

# main

menuBienvenida()

np = numPremisa()  # número de premisas introducidas por el usuario

prem = introPremisas(np)  # lista de premisas introducidas por el usuario

nprop, let = numprop(prem)  # número de proposiciones introducidas por el usario y letras a usar

tablar = renglones(nprop, let)

q = 'q'
p = 'p'

operaciones(prem, nprop, tablar)

print(tabulate(tablar))

'''
negacion(tablar,q,nprop)

conjuncion(tablar,p,q,nprop)

disyuncion(tablar,p,q,nprop)

condicional(tablar,p,q,nprop)

bicondicional(tablar,p,q,nprop)


print(tablar)

print(prem)
'''
