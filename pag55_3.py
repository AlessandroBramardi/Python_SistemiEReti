def main():
    a=int(input("Inserisci il primo numero: "))
    b=int(input("Inserisci il secondo numero: "))
    print("stampa base: ")
    print(f"a = {a}"+ f"b = {b}")
    print("stampa scambiata: ")
    a,b=b,a
    print(f"a = {a}"+ f"b = {b}")

if __name__ == '__main__':
    main()