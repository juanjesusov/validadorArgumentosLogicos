#fcc
import sys

variables=['p','q']

def saludo():
  print ("\nHola, Bienvenido!")

def premisas():
    while True:
        try:
           n = int(input("\n¿Cuántas premisas vas a introducir?: "))
           if (n <= 2 and n>0):
                premisas = []
                valor = []
                for i in range(n):
                    print("\nIntroduce la premisa", variables[i],":")
                    p = input()
                    premisas.append(p)
                    while True:
                        try:
                            v = input("Introduce el valor de la premisa (v o f): ") #v = valor de verdad
                            if v=="v":
                                valor.append(True)
                                break
                            elif v== "f":
                                valor.append(False)
                                break
                            else:
                                print("Por favor solo introduce v o f.")
                        except ValueError:
                            print("Por favor introduce un valor válido.")
                break
           else:
                print("Solo puedes introducir de 1-2 premisas.")
        except ValueError:
            print("Por favor introduce un tipo de valor válido.")
    return premisas, valor, n


def MenuOperaciones(n):
    if n==1:
        while True:
            print("\nMenú\n1. Negación\n6. Salir")
            try: 
                op = int(input("\nEscoge que operación quieres realizar con las premisas: ")) #op es la opción del menú
                if op==1 or op==6:
                    return op
                    break
                else: 
                    print("Ingresa un número valido.")
            except ValueError:
                print("Ingresa solo valores númericos.")
    else:
        while True:
            print("\nMenú\n1. Negación\n2. Conjunción\n3. Disyunción\n4. Condicional\n5. Bicondicional\n6. Salir")
            try: 
                op = int(input("\nEscoge que operación quieres realizar con las premisas: ")) #op es la opción del menú
                if op>=1 and op<=6:
                    return op
                    break
                else: 
                    print("Ingresa un número valido.")
            except ValueError:
                print("Ingresa solo valores númericos.")


def negacion(x,y,n):#x premisa y y valor (verdadero falso)
    v=['p','q']
    print(v[n],"=~",v[n])
    valorverdad=bool(not(y[n]))
    print("La negación de",x[n],"es: ",valorverdad)
    return valorverdad

def conjuncion(x,y):
    v=['p','q']
    print(v[0],"^",v[1])
    valorverdad=bool(y[0] and y[1])
    print("La conjunción de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

def disyuncion(x,y):
    v=['p','q']
    print(v[0],"v",v[1])
    valorverdad=bool(y[0] or y[1])
    print("La disyunción de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

def condicional(x,y):
    v=['p','q']
    print(v[0],"→",v[1])
    if y[0]==True and y[1]==False:
        valorverdad=False
    else:
        valorverdad=True
    print("La condicional de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

def bicondicional(x,y):
    v=['p','q']
    print(v[0],"↔",v[1])
    if y[0]==y[1]:
        valorverdad=True
    else:
        valorverdad=False
    print("La bicondicional de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

ejpremisa=[]
ejvalor=[]

saludo()
ejpremisa, ejvalor, numPrem = premisas()

opmenu=MenuOperaciones(numPrem)
if opmenu==1:
    if numPrem==2:
        while True:
            try:
                print("¿Que premisa quieres negar?")
                np=input("Escoge p o q: ")#np = numero de premisa
                if np=="p":
                    np=int(0)
                    break
                elif np=="q":
                    np=int(1)
                    break
                else:
                    print("Introduce una letra válida.")
            except ValueError:
                print("Introduce un dato válido.")
    elif numPrem==1:
        np=int(0)
    vv=negacion(ejpremisa, ejvalor,np)#np es número de premisa
elif opmenu==2:
    vv=conjuncion(ejpremisa, ejvalor)
elif opmenu==3:
    vv=disyuncion(ejpremisa, ejvalor)
elif opmenu==4:
    vv=condicional(ejpremisa, ejvalor)
elif opmenu==5:
    vv=bicondicional(ejpremisa, ejvalor)
elif opmenu==6:
    print("Salida")
    sys.exit(0)