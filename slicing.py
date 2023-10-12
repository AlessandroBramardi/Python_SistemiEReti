#SLICING =>DIVIDERE
s= "ciao come stai?" #posso indicizzare al contrario c=-4;i=-3;a=-2;o=-1;
print(f"Il primo carattere è {s[0]}")
print(f"L'ultimo carattere è {s[-1]}")
print(f"Il penultimo carattere è {s[-2]}")
print(f"L'ultimo carattere è {s[len(s)-1]}") #C -style da non usare

print(s[3:7]) #dal carattere 3 a 7 escluso
print(s[1:-1]) #dal carattere 1 a -1 escluso
print(s[1:]) #dal carattere 1 fino alla fine
print(s[:-1]) #tutta la stringa tranne ultimo carattere