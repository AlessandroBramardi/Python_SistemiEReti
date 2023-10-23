import math 
def main():
    n=200
    lista=[i**2 for i in range(0, 1000) if (i%2!=0) and (i**2<n)]
    ##lista_quad_disp=[i**2 for i in range(0, int(math.sqrt(n))+1) if i%2!=0]
    print("Caricamento con list comprehension quadrati perfetti dispari:")
    print(lista)
    ##print (lista_quad_disp)
if __name__ == "__main__":
    main()