

def main():
    r=0
    c=0
    i = 0
    list=[]
    r = int(input(""))
    c = int(input(""))
    while i < r*c:
        valor = int(input(""))
        if valor <= 10:
            list.append(valor)
        i = i + 1
    
    print(list)



if __name__=='__main__':
    main()
