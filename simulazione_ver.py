import random

def calcolaSpostamenti(sec=432000,lista=[1,-1]):
    lista_spost=[random.choice(lista) for _ in range(0,sec)]
    print(lista_spost)
    lunghezza=0
    for val in lista_spost:
        lunghezza+=val
    print(lunghezza)

def main():
    sec = 432000
    lista=[1,-1]
    calcolaSpostamenti(lista=[3,-3]) #passaggio di parametri con valore di def

if __name__ == "__main__":
    main()