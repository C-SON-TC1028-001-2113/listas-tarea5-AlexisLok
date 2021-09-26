def main():
    #escribe tu código abajo de esta línea


    n= int(input("")) #Se pide el número de valores en la lista
    #Se establecen las listas vacias para capturar
    list=[] 
    listCom=[]
    
    #Se establece un if para conocer si n es un valor aceptado
    if n > 1 :
        
        #Ciclo para agregar valores a lista
        for x in range(0,n):
            valor = input("")
            listCom.append(valor) #Se llena la lista sin borrar valores
            if valor not in list: #El if evalua si el valor se encuentra en la lista
                list.append(valor)

        #Se imprimen la lista completa y la modificada
        print(listCom)
        print(list)
        
    else:
        print("Error") 
 
if __name__=='__main__':
    main()
