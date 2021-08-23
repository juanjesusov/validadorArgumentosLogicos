from tabulate import tabulate

variables=['p','q']

def menuBienvenida():
    print("\n\t¡Hola, Bienvenido a la Calculadora de Valor de Verdad!")
    print("Selecciona la opción que quieras usar: \n1.Valor de verdad premisas\n2.Validez de argumento y tabla de verdad\n3.Salir")
    i=int(input("Opción: "))
    if i==1:
        print("\nPremisas")
    elif i==2:
        print("\nCalculadora de Tablas de Verdad\nInstrucciones para usar la calculadora: \n1. Solo puedes usar las proposiciones p, q, r, s, t \n2. Utiliza operaciones sencillas no compuestas\n")
        print("Operadores por Jerarquía\nNegación: ~ (alt+126) \nConjunción: ^ (alt+94)\nDisyunción: v (letra)\nCondicional: → (copiar y pegar)\nBicondicional: ↔ (copiar y pegar)")
    elif i==3:
        print("Gracias por usar la herramienta.")
    return i

def premisas():
    while True:
        try:
           n = int(input("¿Cuántas premisas vas a introducir?: "))
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
                op = int(input("\nEscoge que operación quieres realizar con las premisas(1-6): ")) #op es la opción del menú
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


def negacion1(x,y,n):#x premisa y y valor (verdadero falso)
    v=['p','q']
    print(v[n],"=~",v[n])
    valorverdad=bool(not(y[n]))
    print("La negación de",x[n],"es: ",valorverdad)
    return valorverdad

def conjuncion1(x,y):
    v=['p','q']
    print(v[0],"^",v[1])
    valorverdad=bool(y[0] and y[1])
    print("La conjunción de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

def disyuncion1(x,y):
    v=['p','q']
    print(v[0],"v",v[1])
    valorverdad=bool(y[0] or y[1])
    print("La disyunción de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

def condicional1(x,y):
    v=['p','q']
    print(v[0],"→",v[1])
    if y[0]==True and y[1]==False:
        valorverdad=False
    else:
        valorverdad=True
    print("La condicional de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

def bicondicional1(x,y):
    v=['p','q']
    print(v[0],"↔",v[1])
    if y[0]==y[1]:
        valorverdad=True
    else:
        valorverdad=False
    print("La bicondicional de",x[0], "y",x[1],"es:",valorverdad)
    return valorverdad

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
            print("Introduce la conclusión: ")
            po = input()
        else:
            print("Introduce la premisa número", i + 1, ": ")
            po = input()
        p.append(po.replace(" ", ""))
    return p

def numprop(p):
    simbolos = ["~", "^", "v", "→", "↔", "(", ")"]
    strp = "".join(p) #elimina espacios de enunciados
    pr = list(strp)
    pr = [q for q in pr if q not in simbolos]  # enunciado sin símbolos
    return len(set(pr)), pr  # regresa el número de letras (p q r s t)


def renglones(n, pr):
    renglon = 2 ** n  # número de renglones
    tabla = []
    pr = list(set(pr))
    for i in range(n):
        tabla.append(pr[i:i + 1])
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
            a, b = strp[k - 1], strp[k + 1]  # letra que se usara en la operación
            conjuncion(tabla, a, b, n)
        elif i == 'v':
            a, b = strp[k - 1], strp[k + 1]  # letra que se usara en la operación
            disyuncion(tabla, a, b, n)
        elif i == '→':
            a, b = strp[k - 1], strp[k + 1]  # letra que se usara en la operación
            condicional(tabla, a, b, n)
        elif i == '↔':
            a, b = strp[k - 1], strp[k + 1]  # letra que se usara en la operación
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

def validez(tabla,pre):
    ntabla=[]
    for i in pre:
        for j in tabla:
            if i==j[0]:
                ntabla=ntabla+[j] #crear nueva tabla con valores de verdad de premisas y conclusion
    value=True #valor de verdad inicial de premisas
    co=len(ntabla[0])#numero de renglones
    ult=len(ntabla)-1#ultima columna (conclusion)
    fin = "El argumento es válido."
    for i in range(1,co):#ciclo para recorrer renglones
        for j in range(len(ntabla)-1):#ciclo para recorrer premisas
            value=value and ntabla[j][i] #compara valores de premisa
        if value==True and ntabla[ult][i]==False: #compara valor de premisa con conclusion (condicional)
            fin="El argumento no es válido." #el argumento es invalido si hay excepcion
        value = True
    return fin


ip=0
while ip!=3: #ciclo para mostrar menu de bienvenida
    ip=menuBienvenida()
    if ip==1: #opcion 1 premisas sencillas
        ejpremisa, ejvalor, numPrem = premisas()
        opmenu = MenuOperaciones(numPrem)
        if opmenu == 1:
            if numPrem == 2:
                while True:
                    try:
                        print("¿Que premisa quieres negar?")
                        np = input("Escoge p o q: ")  # np = numero de premisa
                        if np == "p":
                            np = int(0)
                            break
                        elif np == "q":
                            np = int(1)
                            break
                        else:
                            print("Introduce una letra válida.")
                    except ValueError:
                        print("Introduce un dato válido.")
            elif numPrem == 1:
                np = int(0)
            vv = negacion1(ejpremisa, ejvalor, np)  # np es número de premisa
        elif opmenu == 2:
            vv = conjuncion1(ejpremisa, ejvalor)
        elif opmenu == 3:
            vv = disyuncion1(ejpremisa, ejvalor)
        elif opmenu == 4:
            vv = condicional1(ejpremisa, ejvalor)
        elif opmenu == 5:
            vv = bicondicional1(ejpremisa, ejvalor)
        elif opmenu == 6:
            print("Salida")
    elif ip==2: #menu tabla de verdad
        np = numPremisa()  # número de premisas introducidas por el usuario
        prem = introPremisas(np)  # lista de premisas introducidas por el usuario
        nprop, let = numprop(prem)  # número de proposiciones introducidas por el usario y letras a usar
        tablar = renglones(nprop, let) #crea primeros renglones con valores de verdad
        operaciones(prem, nprop, tablar) #saca el valor de verdad de las operaciones
        print(tabulate(tablar)) #imprime tabla de verdad
        print(validez(tablar,prem)) #comprueba validez del argumento
