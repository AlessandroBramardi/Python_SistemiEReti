import turtle
finestra = turtle.Screen()
tarta = turtle.Turtle()
tarta.speed(3)  
n = int(input("Inserisci il numero di punte della stella: "))
lunghezza = 100
angolo_interno = 180/n
tarta.begin_fill()
for i in range(0,n):
    tarta.forward(lunghezza)
    tarta.left(180-angolo_interno)
tarta.end_fill()

finestra.mainloop()
