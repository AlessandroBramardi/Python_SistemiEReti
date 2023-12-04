import turtle

def quadrato(lato, tarta):
    for _ in range(4):
        tarta.forward(lato)
        tarta.left(90)
    tarta.forward(lato)
    
def disegnaGriglia(lato,tarta):
    for _ in range(4):
        for _ in range(4):
            quadrato(lato,tarta)
        tarta.left(90)
        tarta.forward(lato)
        tarta.left(90)
        tarta.forward(lato*4) #deve tornare indietro
        tarta.left(180) #si deve girare per riniziare a scrivere

def main():
    finestra=turtle.Screen()
    tarta=turtle.Turtle()
    tarta.speed("fast")
    lato = 10
    disegnaGriglia(lato,tarta)
    finestra.mainloop()

if __name__ == "__main__":
    main()