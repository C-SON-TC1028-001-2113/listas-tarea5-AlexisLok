

def main():
    r=0
    c=0
    i = 0
    list=[]
    r = int(input("")) #Establece renglones de matriz
    c = int(input("")) #Columnas de matriz
    #Se realiza un ciclo para tomar los datos de la matriz 
    while i < r*c: 
        valor = int(input(""))
        if valor < 10: #Si los valores son menores a 10, se agregan a la lista
            list.append(valor)
        i = i + 1
    
    print(list) #Se imprime la lista



if __name__=='__main__':
    main()
