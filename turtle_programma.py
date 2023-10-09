import turtle
n=int(input("Inserisci il numero di lati: "))
finestra = turtle.Screen()
benny = turtle.Turtle()
gradi=360/n
lung=int(input("Inserisci la lunghezza del lato: "))
benny.color("blue")
benny.begin_fill()
benny.speed(5)
for i in range(0,n):
    benny.forward(lung)
    benny.left(gradi)
benny.end_fill()     
finestra.mainloop()