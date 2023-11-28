
def cercaNome(nome,rubrica):
    found = False
    for contatto in rubrica:
        if nome == contatto:
            print(f"Numero di telefono di {nome}: {rubrica[contatto]}")
            found = True
            break
    if found == False:
        print("Nome non trovato")
        
def cercaNum(numero,rubrica):
   found = False
   for nome, num in rubrica.items():
        if num == numero:
            print(f"Contatto con numero {numero}: {nome}")
            found = True
            break
   if found == False:
       print("Numero non trovato")
        
        

def main():
    rubrica = {"Brama": "3775292413", "Gianni": "3332927458"}
    a = int(input("Cosa vuoi cercare: 1 per nome, 2 per numero:"))
    if a == 1:
        nome=input("Inserisci il nome da cercare:")
        cercaNome(nome,rubrica)
    elif a == 2:
        numero=input("Inserisci il numero da cercare:")
        cercaNum(numero,rubrica)
    for x in rubrica:
        if(rubrica[x]=="Brama"):
            print(x)
if __name__ == "__main__":
    main()