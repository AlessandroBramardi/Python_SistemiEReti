a = float(input("Inserisci un numero: "))
print(f"il tipo di a è {type(a)}")
if a>5:
    print("a è maggiore di 5")
elif (a<=5) & (a>=0):
    print("a è compreso tra 0 e 5")
else:
    print("a è minore di 0")