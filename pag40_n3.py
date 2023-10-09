def main():
    op=int(input("Quale operazione vuoi svolgere: 0:somma, 1:sottrazzione, 2:moltiplicazione, 3:divisione: "))
    a=float(input("Inserire il primo numero: "))
    b=float(input("Inserire il secondo numero: "))

    if op==0:
        ris=a+b
    if op==1:
        ris=a-b
    if op==2:
        ris=a*b
    if op==3:
        ris=a/b
    print(f"Risultato: {ris}")

if __name__ == "__main__":
    main()
