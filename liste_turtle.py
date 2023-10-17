import turtle

def movimento(lista):
    finestra = turtle.Screen()
    tarta=turtle.Turtle()
    tarta.speed("slow")
    for elemento in lista:
            if elemento=="f":
                tarta.forward(100)
            if elemento=="r":
                tarta.right(90)
            if elemento=="l":
                tarta.left(90)
    finestra.mainloop()


def main():
    lista = []
    comandiPossibili = ["f", "r", "l"]
    com = "f"
    while com in comandiPossibili:
        com = input("Inserisci un comando e per uscire: ")
        if com in comandiPossibili: 
            lista.append(com) #permette di aggiungere
    movimento(lista)


if __name__ == '__main__':
    main()