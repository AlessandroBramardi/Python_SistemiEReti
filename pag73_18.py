def main():
    n=200
    lista_quad_disp=[i*i for i in range(n) if i%2!=0]
    print("Caricamento con list comprehension quadrati perfetti dispari:")
    print(lista_quad_disp)
if __name__ == "__main__":
    main()