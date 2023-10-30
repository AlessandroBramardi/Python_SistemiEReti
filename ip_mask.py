def main():
    n=int(input("Inserire il numero della barra tra 1 e 31:"))
    ip = "1"*n + "0"*(32-n)
    print(ip)
    gruppo1=ip[0:8]
    gruppo2=ip[8:16]
    gruppo3=ip[16:24]
    gruppo4=ip[24:32]
    lista=[gruppo1,gruppo2,gruppo3,gruppo4]
    print(lista)
    print(".".join(lista))
    lista=[int(gruppo,2) for gruppo in lista]
    print(lista)
    print(".".join(map(str,lista)))
  
if __name__ == "__main__":
    main()