def somma(a,b):
    return a+b

def prodotto(a,b):
    return a*b

def sottrazzione(a,b):
    return a-b

def divisione(a,b):
    return a/b

def main():
    dizionario = {"+":somma, "-":sottrazzione, "/":divisione,"*":prodotto}
    operazione=input("Che operazione vuoi fare: + per somma, * per moltiplicazione, - per sottrazzione e / per divisione: ")
    a = float(input("Scrivi il primo numero: "))
    b = float(input("Scrivi il secondo numero: "))
    print(dizionario[operazione](a,b)) #dizionario ha come valori delle funzioni quindi mi comporto come tale

if __name__ == "__main__":
    main()