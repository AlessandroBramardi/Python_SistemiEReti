# Le liste

def print_list(l):
    print("La lista è: ",end=" ")
    for elemento in l:
        print(elemento,end=" ")
    print("\n")

def main():
    l = [1, 2, 3, "c", 3.14,"python"]
    r = [4, 5, 6, 7, 8, 9]
    #print_list(l)
    print_list(l[::-1])
    print_list(l+r) #concatena l e r
    print_list(r+l) #concatena r e l
    print_list(l*3) #concatena l 3 volte

    #facciamo carica la lista all'utente
    lista = []
    num = 1
    while num>0:
        num = int(input("Inserisci un numero (-1 per interrompere): "))
        if num>0:
            lista.append(num) #permette di aggiungere
            
    print_list(lista)

if __name__ == "__main__":
    main()