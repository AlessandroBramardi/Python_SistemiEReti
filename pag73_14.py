class Quadrato:
    def __init__(self, lato):
        self.lato=lato
    def calcoloArea(self):
        return self.lato*self.lato
    def calcoloPerimetro(self):
        return self.lato*4
    def stampa(self):
        return f"Area: {self.calcoloArea()} Perimetro: {self.calcoloPerimetro()}" 
    def puntoInterno(self,x,y):
        if(x>0 and x<self.lato and y>0 and y<self.lato):
            return True
        else:
            return False
def main():
    quadrato1 = Quadrato(3)
    quadrato2 = Quadrato(10)
    print(quadrato1.stampa())
    print(quadrato1.puntoInterno(4,5))
    print(quadrato2.stampa())
    print(quadrato2.puntoInterno(4,5))


if __name__ == "__main__":
    main()