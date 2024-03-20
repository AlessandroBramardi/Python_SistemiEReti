class Testo:
    def __init__(self, testo):
        self.testo=testo
        self.lista = self.lista_parole()
    def numero_caratteri(self):
        return len(self.testo)
    def lista_parole(self):
        return self.testo.split()
    def lunghezze_parole(self):
        return [len(parola) for parola in self.lista]
    def ricerca(self,parola):
        if parola in self.testo:
            return True
        else:
            return False
    def file(self,nomefile):
        with open(nomefile, "w") as f:
            f.write(self.testo)
    def frequenze_parola(self):
        diz_freq = {}
        for parola in self.lista:
            if parola in diz_freq:
                diz_freq[parola] += 1
            else:
                diz_freq[parola] = 1
        return diz_freq
        
    
def main():
    prova = "ciao come stai, ciao sto bene"
    t = Testo(prova)
    print(t.numero_caratteri())
    print(t.lista_parole())
    print(t.lunghezze_parole())
    print(t.ricerca("ciao"))
    t.file("correzzione.txt")
    print(t.frequenze_parola())
    
    

if __name__ == "__main__":
    main()