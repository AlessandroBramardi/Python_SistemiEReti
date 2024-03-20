def main():
    n = int(input("Inserire un numero dispari: "))
    while(n%2==0):
        print("Il numero inserito è pari, reinseriscilo!")
        n = int(input("Inserire un numero dispari: "))
        
    for i in range(1, n, 2):
        print(' ' * ((n - i) // 2) + '*' * i)

    for i in range(n, 0, -2):
        print(' ' * ((n - i) // 2) + '*' * i)
            
if __name__ == "__main__":
    main()