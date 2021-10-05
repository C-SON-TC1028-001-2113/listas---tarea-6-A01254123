def main():     #Fuente: https://www.delftstack.com/es/howto/python/fibonacci-sequence-python/
    i=-1
    lista=[]
    a=1
    b=1
    total=0
    while i<=-1:
        i= int(input())
    if i==1:
        lista.append(0)
        print(lista)
    elif i==2:
        lista.append(0)
        lista.append(1)
        print(lista)
    elif i==0:
        print(lista)
    else:
        lista.append(0)
        lista.append(1)
        lista.append(1)
        for x in range(i-3):
            total=a+b
            b=a
            a=total
            lista.append(total)
        print(lista)    
if __name__=='__main__':
    main()