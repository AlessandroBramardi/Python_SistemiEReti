#chiede due numeri all'utente e stampi una stringa con dentro i numeri in ordine decrescente

a=float(input("Inserisci il primo numero "))
b=float(input("Inserisci il secondo numero "))

if a<b:
    #mag=a
    #minore=b
    b, a = a, b
print(f"{a} {b}")