import turtle
import random

class Punto():
    def __init__(self, x, y):
         self.x=x
         self.y=y
         

def nord(lunghezza,f,tarta,posizioni):
    f.write("bob si sposta di 10 metri verso nord \n")
    tarta.setheading(90)
    tarta.forward(lunghezza)
    posizione= tarta.pos()
    if posizione in posizioni:
        print(f"bob è passato di nuovo in {posizione}")
    else:
            posizioni.append(posizione)
    

def sud(lunghezza,f,tarta,posizioni):
    f.write("bob si sposta di 10 metri verso sud \n")
    tarta.setheading(270)
    tarta.forward(lunghezza)
    posizione= tarta.pos()
    if posizione in posizioni:
        print(f"bob è passato di nuovo in {posizione}")
    else:
            posizioni.append(posizione)
    
    

def est(lunghezza,f,tarta,posizioni):
    f.write("bob si sposta di 10 metri verso est \n")
    tarta.setheading(0)
    tarta.forward(lunghezza)
    posizione= tarta.pos()
    if posizione in posizioni:
        print(f"bob è passato di nuovo in {posizione}")
    else:
            posizioni.append(posizione)
    
    

def ovest(lunghezza,f,tarta,posizioni):
    f.write("bob si sposta di 10 metri verso ovest \n")
    tarta.setheading(180)
    tarta.forward(lunghezza)
    posizione= tarta.pos()
    if posizione in posizioni:
        print(f"bob è passato di nuovo in {posizione}")
    else:
            posizioni.append(posizione)
    
    

def spostamenti(lunghezza, dizionario_spost,tarta):
    lista=[1,2,3,4]
    posizioni = []
    f = open("bob_spost.csv","w")
    
    for _ in range(60):
        spost=dizionario_spost[random.choice(lista)]
        if spost == "nord":
            nord(lunghezza,f,tarta,posizioni)
        elif spost == "sud":
            sud(lunghezza,f,tarta,posizioni)
        elif spost == "est":
            est(lunghezza,f,tarta,posizioni)
        elif spost == "ovest":
            ovest(lunghezza,f,tarta,posizioni)
    f.close()
    
            
        

def main():
    tarta=turtle.Turtle()
    finestra=turtle.Screen()
    tarta.goto(0,0)
    tarta.speed("fast")
    lunghezza = 10
    percorso = {0:Punto(0,0)}
    for tempo in range(1,60):
        pass
    dizionario_spost = {1:"nord", 2: "sud", 3: "est", 4: "ovest"}
    spostamenti(lunghezza,dizionario_spost,tarta)
    finestra.mainloop()
    
    

if __name__ == "__main__":
    main()