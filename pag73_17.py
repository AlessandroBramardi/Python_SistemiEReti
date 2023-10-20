def main():
    n=(int(input("Inserisci la soglia massima:")))
    lista_potenze=[i*i for i in range(n+1)];
    print("Caricamento con list comprehension")
    print(lista_potenze)
if __name__ == "__main__":
    main()
    