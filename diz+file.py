def main():
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