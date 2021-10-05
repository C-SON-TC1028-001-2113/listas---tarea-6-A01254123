def menores(matriz):
    menores=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]<10:
                menores.append(matriz[i][j])
    return menores

def main():
    elementrosMatriz=[]
    filas=int(input())
    columnas=int(input())  
    for i in range(filas):
        elementrosMatriz.append([])
        for j in range(columnas):
            datosMatriz=int(input())
            elementrosMatriz[i].append(datosMatriz)
    menoresDiez=menores(elementrosMatriz)
    print(menoresDiez)

if __name__=='__main__':
    main()