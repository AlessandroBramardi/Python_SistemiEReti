class Classe():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def somma(self):
        return self.x+self.y
    
    
def somma(x,y):
    return x+y

def diff(x,y):
    return x-y
    
def main():
    lista = [x*2 for x in range(0,10) if x!=20] #list comprension
    print(lista)
    c = Classe(30,40) #classse
    print(c.somma())
    diz = {"somma": somma, "differenza": diff} #dizionari
    oper = input("Vuoi la somma o la sottrazione: ")
    print(diz[oper](40,50))
    parola="ciao come stai?"
    parola_consonanti="".join([c*2 if c not in "aeiou" else c for c in parola]) #raddoppio i caratteri
    print(parola)
    print(parola_consonanti)
    with open("prova.txt","r") as file:
        str = file.readlines()
    print(str)
    
    with open("prova.txt", "a") as file:
        file.write("tutto bene tu")

    frase = "bella per gioggis"
    pezzi_frase = frase.split() #divide per gli spazi
    print(pezzi_frase)

    
    f = open("rubrica.txt", "r")
    righe = f.readlines()
    rubrica = {}
    #caricamento rubrica da file
    for riga in righe:
        campi=riga.split(", ") #creo una lista di campi 
        nome=campi[0] #salva nome
        numero_tel=(int(campi[1].replace("\n",""))) #salva numero #replace sostituisce campi
        rubrica[numero_tel] = nome
    print(rubrica)        
    f.close()

if __name__ == "__main__":
    main()