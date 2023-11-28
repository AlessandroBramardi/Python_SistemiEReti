class Robot:
    def __init__(self,nome,massa,umanoide):
        self.nome=nome
        self.massa=massa
        self.umanoide=umanoide
    def stampa(self):
        print(f"Nome: {self.nome} massa: {self.massa} ")
        if self.umanoide==True:
            print("umanoide")
        else:
            print("non è umanoide")
    def isPericoloso(self):
        if self.umanoide==True and self.massa>100:
            return True
        else:
            return False
        

def main():
    robot1 = Robot(nome="Gianni", massa=190, umanoide=True)
    robot1.stampa()
    if robot1.isPericoloso()==True:
        print("E' pericoloso!")
    else:
        print("Non è pericoloso")


if __name__ == "__main__":
    main()