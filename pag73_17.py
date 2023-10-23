import math
def main():
    n=int(input("Inserisci la soglia massima:"))
    esponente=n**2
    lista_potenze=[2**i for i in range(0,esponente) if (2**i<=n)]
    print("Caricamento con list comprehension")
    print(lista_potenze)
if __name__ == "__main__":
    main()
    