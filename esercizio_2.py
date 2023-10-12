def main(): #definizione della funzione main
    a=1
    print(f"il valore di a è {a}")
    nome=input("Come ti chiami? ")
    anni=int(input("Quanti anni hai? ")) #è una stringa anche se è un numero
    anno_corrente=int(input("In che anno siamo? "))
    print(f"Ti chiami {nome} e hai {anni}") #uso f per concatenare stringhe e salvare variabili!
    #print(type(anni)) ci dice il tipo di variabile
    print(f"Sei nato nell'anno {anno_corrente-anni}")
    print("va a capo da solo")
if __name__ == "__main__":
    main()