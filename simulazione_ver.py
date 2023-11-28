import random

def spostamento():
    lista=[1,-1]
    return random.choice(lista)

def calcolaSpostamenti():
    sec = 432000
    lista_spost=[spostamento() for _ in range(0,sec)]
    print(lista_spost)
    lunghezza=0
    for val in lista_spost:
        lunghezza+=val
    print(lunghezza)

def main():
    calcolaSpostamenti()

if __name__ == "__main__":
    main()