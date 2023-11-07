def main():
    #il dizionario è una collezzione di coppie (chiave e valore)
    #non ha indici ma si indicizza per chiave
    dizionario = {"nome": "mario","cognome":"rossi"} #nome chiave mario valore, cognome chiave rossi valore
    #lista = ["mario","rossi"]
    print(dizionario["nome"])
    #aggiunge un elemento nuovo al dizionario
    dizionario["data nascita"] = "01/01/1900"
    #aggiunge due elementi nuovi
    dizionario["eta"] = "123"
    print(dizionario)
    dizionario["nome"] = "luca" #sostituisce in base alla chiave
    print(dizionario)
    #cicli sui dizionari
    for x in dizionario: #x scorre sulle chiavi
        print(f"chiave: {x} - valore: {dizionario[x]}")
    rubrica = {3775292413: "Brama", 3335687432: "Giorgis"}
    for x in rubrica:
        if(rubrica[x]=="Brama"):
            print(x)
if __name__ == "__main__":
    main()