import turtle

def nord(lung,tarta):
    tarta.setheading(90)
    tarta.forward(lung)

def sud(lung,tarta):
    tarta.setheading(270)
    tarta.forward(lung)

def est(lung,tarta):
    tarta.setheading(0)
    tarta.forward(lung)

def ovest(lung,tarta):
    tarta.setheading(180)
    tarta.forward(lung)
    

def main():
    finestra = turtle.Screen()
    lung = 100
    tarta=turtle.Turtle()
    tarta.speed("slow")
    dizionario= {"nord": nord, "sud": sud, "est": est, "ovest": ovest}
    while(True):
        movimento=input("Inserire dove vuoi mandare la turtle: ")
        if movimento in dizionario:
            dizionario[movimento](lung,tarta)
        else:
            break    
    finestra.mainloop()
    

if __name__ == "__main__":
    main()