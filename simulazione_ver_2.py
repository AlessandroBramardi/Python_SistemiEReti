import turtle

def disegnaGriglia(lato,tarta):
    pass

def main():
    finestra=turtle.Screen()
    tarta=turtle.Turtle()
    tarta.speed("slow")
    lato = 10
    disegnaGriglia(lato,tarta)
    
    
    finestra.mainloop()

if __name__ == "__main__":
    main()