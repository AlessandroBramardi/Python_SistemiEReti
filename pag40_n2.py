def main():
    a=int(input("Inserisci un numero: "))
    if a%2 == 0:
        print("E' divisibile per 2")
    elif a%3 == 0:
        print("E' divisibile per 3")
    elif a%5 == 0:
        print("E' divisibile per 5")
    else :
        print("Non è divisibile per nessun numero")

if __name__ == "__main__":
    main()