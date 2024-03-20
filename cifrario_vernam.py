'''
classe testo deve poter vedere sia testo codificato che non
'''

diz_let={0:"a", 1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"l",10:"m",11:"n",12:"o",13:"p",14:"q",15:"r", 16:"s",17:"t",18:"u",19:"v",20:"z"}
diz_num={}
for numero in diz_let:
    diz_num[diz_let[numero]] = numero #creo dizionario opposto

class Testo:
    def __init__(self,testo,chiave,codifica):
        self.testo=testo
        self.chiave=chiave
        self.codifica=codifica
    def cifra_cod(self):
        if self.codifica== False:
            lista_chiave = [c for c in self.chiave]
            cifra=[]
            for k,c in enumerate(self.testo):
                cifra.append((diz_let[c] + diz_let[lista_chiave[k]])%21)
            self.codifica=True
            print(cifra)
        else:
            print("la stringa è già cifrata")
            
    def decod(self):
        if self.codifica==True:
            lista_chiave = [c for c in self.chiave]
            cifra = []
            for c,k in enumerate(self.cifra):
                
            
                    
                    
        
def main():
    str = input("inserire una stringa: ")
    chiave = input("inserire la chiave per cifrare: ")
    str_cod = Testo(str,chiave,codifica=True).vernam()
    str_decod = Testo(str_cod,chiave,codifica=False).vernam()
    print(f"Testo codificato: {str_cod}")
    print(f"Testo decodificato: {str_decod}")
    
        

if __name__ == "__main__":
    main()