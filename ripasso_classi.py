import random
class Nemico():
    def __init__(self, pos_x, pos_y, n_vite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.n_vite = n_vite
    def stampa(self):
        print(f"Nemico in posizone: {self.pos_x} \ {self.pos_y} con {self.n_vite} vite")
        
def main():
    N_NEMICI = 5
    WIDTH = 800
    HEIGHT = 400
    lista_nemici=[]
    random.seed(1234) #genera il seme per il random
    for _ in range(N_NEMICI):
        pos_x=random.randint(0,WIDTH-1) #include gli estremi
        pos_y=random.randint(0,HEIGHT-1)
        nemico = Nemico(pos_x,pos_y,5)
        lista_nemici.append(nemico)
    personaggio = {"pos_x": 180, "pos_y": 200}
    for nemico in lista_nemici:
        nemico.stampa()
        if (nemico.pos_x==personaggio["pos_x"]) and (nemico.pos_y==personaggio["pos_y"]):
            print("COLLISIONE")
        

if __name__ == "__main__":
    main()