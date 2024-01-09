def push(pila,elemento):
    pila.append(elemento)
    
def pop(pila):
    if len(pila)==0:
        x = None #null del c
    else:
        x = pila.pop()
    return x


def main():
    parentesi_aperte=["{", "[", "("]
    parentesi_chiuse=["}", "]", ")"]
    dizionario = {"{":"}", "[":"]","(":")"}
    stringa = "]{1+[2+3]*5[}"
    pila = [] 
    errore = False
    cont = 0
    pos_errore = None
    for pos_carattere, carattere in enumerate(stringa):
        if carattere in parentesi_aperte: 
            push(pila,carattere)
        if carattere in parentesi_chiuse:
                parentesi=pop(pila)
                if parentesi != None:
                    if dizionario[parentesi]!=carattere: #confronta con il dizionario
                        errore=True
                        pos_errore = pos_carattere    
                else:
                    errore = True
                    pos_errore = pos_carattere
        cont+=1
    if errore:
        print(f"Errore! posizione:{pos_errore}")
    else:
        print("Corretto!")        
        
if __name__ == "__main__":
    main()