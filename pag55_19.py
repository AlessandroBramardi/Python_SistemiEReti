import math


def media_aritmetica(x,y):
    media = (x+y) / 2
    return media

def media_geometrica(x,y):
    media = math.sqrt(x*y)
    return media


def main():
    x = int(input("Inserisci il primo numero: "))
    y = int(input("Inserisci il secondo numero: "))
    dizionario = {"media_aritmetica": media_aritmetica(x,y), "media_geometrica": media_geometrica(x,y)}
    print(dizionario)

if __name__ == "__main__":
    main()