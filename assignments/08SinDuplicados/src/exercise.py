def main():
    #escribe tu código abajo de esta línea
    n= int(input(""))
    list=[]
    con = 0
    i = 0
   
 
    if n > 1 :
        while i < n:
            valor = input("")
            list.append(valor)
            i += 1
        
        for x in range(0,n+1):
            valor = list[con]
            print(valor)

            while con < n:
                borrar = list[x+1]
                if borrar == valor:
                    del list[x+1]
                con = con +1

        #while n>con:
         #   valor = list[con]
            
          #  while n> x+1:
           #     if valor == list[x]:
            #        del list[x]
             #   x+=1
            #con += 1
 
        print(list)
        
    else:
        print("Error")
 
 
if __name__=='__main__':
    main()
