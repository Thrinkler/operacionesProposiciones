## codigo hecho por Thrinkler

# NOT = !
# AND = &
# OR  = |
# XOR = ^
# DISYUNCION INCLUSIVA  (~a) | b
# DISYUNCION EXCLUSIVA  (~a) ^ b      ####((not a) or b) & (not b) or a)

def din(p,q):
    return((not p) | q)                 ## python no contiene ni disyuncion inclusiva ni exclusiva, nosotros creamos
def dex(p,q):                           ## dos variables din() y dex() para emular dichas disyunciones
    return((not p) ^ q)

n = int(input("numero de variables: "))
l = 2**n
linicial = [[i>>j&1 for j in range(n-1,-1,-1)] for i in range(l-1, -1, -1)]    ## una version corta para hacer una combinatoria de verdaderos y falsos empezando
                                                                        ## todos verdaderos y terminando todos falsos
menu = """
# NOT = not
# AND = &
# OR  = |
# XOR = ^
# DISYUNCION INCLUSIVA din(a,b)  (not a) | b
# DISYUNCION EXCLUSIVA dex(a,b)  (not a) ^ b

favor de notar las variables como r[]
ejemplo: (not r[0]) or (r[1])
"""
while True:
    print(menu)
    for row in linicial: print(row)                     ## imprimimos la lista con la que trabajaremos
    
    operacion = input("dime la operacion ")         
    lista = [int(eval(operacion)) for r in linicial]    ## Con la operacion dada, hacemos la operacion con la lista inicial

    if lista[0] in (0,1):
        if all(i== lista[0] for i in lista):            ## comparamos si todos los valores son iguales en la lista
            if lista[0] == True:
                print("Es tautologica\n")               ## si son todos verdaderos, se llama tautologia
            else:
                print("Es contradictoria \n")           ## si son todos falsos, se llama contradiccion
        else:
            print("Es una contingencia\n")              ## si los valores no son todos iguales, se llama contingente.

        for f in range(len(linicial[0])):
            print(f)
            if all(linicial[n][f]==i for n,i in enumerate(lista)):             ## Comparamos nuestra nueva lista con los valores pasados y vemos si se parecen.
                print("esta expresion es logicamente equivalente a la fila "+str(f+1))

        for n,valores in enumerate(linicial):
            valores.append(lista[n])                          ## Finalmente almacenamos la lista en nuestra primera lista para hacer mas trabajos con ella

    else:
        print("no pusiste un valor valido")                   ## failsave
    for row in linicial: print(row)
    option = input("\nQuieres hacer una segunda operacion\nusando la lista anterior y los conjuntos? Y/N\n")  ## si pone y,Y,s o S, repetimos el codigo.
    if( option.lower() not in ("y", "s") ): break












