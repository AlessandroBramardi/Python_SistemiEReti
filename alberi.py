class Node():
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None
        
    def inserisci(self, valore):
        if valore < self.valore:
            if self.sinistro is None:
                self.sinistro = Node(valore)
            else:
                self.sinistro.inserisci(valore)
        elif valore > self.valore:
            if self.destro is None:
                self.destro = Node(valore)
            else:
                self.destro.inserisci(valore)
       
    
    def printTree(self):
        if self.valore is not None:
            if self.sinistro is not None:
                self.sinistro.printTree()
            print(self.valore)
            if self.destro is not None:
                self.destro.printTree()
            
    def find(self, valore):
        if self.valore is not None:
            if valore == self.valore:
                return True
            elif valore < self.valore and self.sinistro is not None:
                return self.sinistro.find(valore)
            elif valore > self.valore and self.destro is not None:
                return self.destro.find(valore)
        return False
            
        
def caricamentoLista(lista,ordinato):
    if ordinato==False:
        lista.sort()
        centro = len(lista) // 2
        n = Node(lista[centro])
        ordinato=True
    else:
        n.sinistro = caricamentoLista(lista[:centro])
        n.destro = caricamentoLista(lista[centro+1:])
        return n
            
        
def main():
    n = Node(5)
    n.inserisci(2)
    n.inserisci(10)
    n.inserisci(1)
    n.inserisci(7)
    n.printTree()
    print(n.find(7))
    lista_nodi = [5,6,2,20,28,16]
    albero_bin=caricamentoLista(lista_nodi,False)
    albero_bin.printTree()
    
    
if __name__ == '__main__':
    main()
