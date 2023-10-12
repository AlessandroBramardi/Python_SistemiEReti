import turtle
def main():
    finestra=turtle.Screen()
    tarta=turtle.Turtle()

    #def disegnaPoligono(t, num, lato):
        #gradi=360/num
        #t.begin_fill()
        #for i in range(0,num):
            #t.forward(lato)
            #t.right(gradi)
        #t.end_fill()

    tarta.shape("turtle")
    lati=3
    tarta.speed(3)
    tarta.penup()
    tarta.left(90)
    tarta.forward(110)
    tarta.right(90)
    tarta.backward(275)
    tarta.pendown()

    for j in range(0,3):
        for k in range(0,3):
            for i in range(0,lati):
                if lati <= 5:
                    tarta.forward(100)
                else:
                    tarta.forward(50)
                tarta.left(360/lati)
            lati+=1
            tarta.penup()
            tarta.forward(200)
            tarta.pendown()
        tarta.penup()
        if lati <= 8:
            tarta.back(575)
        else:
            tarta.back(600)
        tarta.right(90)
        if lati <= 8:
            tarta.forward(150)
        else:
            tarta.forward(200)
        tarta.left(90)
        tarta.pendown()
        #disegnaPoligono(tarta, lati, 100)
        
    finestra.mainloop()

if __name__ == "__main__":
    main()