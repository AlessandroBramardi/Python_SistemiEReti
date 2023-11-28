def f1(x,y):
    somma = (x**2)+(y**2)
    return somma

def f2(x,y):
    quad = (x+y)**2
    return quad

def f3(x,y):
    diff = (x**2)-(y**2)
    return diff

def f4(x,y):
    quad_diff = (x-y)**2
    return quad_diff
    

def main():
    x = int(input("Inserisci il primo numero: "))
    y = int(input("Inserisci il secondo numero: "))
    lista = [f1(x,y),f2(x,y),f3(x,y),f4(x,y)]
    print(lista)
    
    
if __name__ == "__main__":
    main()