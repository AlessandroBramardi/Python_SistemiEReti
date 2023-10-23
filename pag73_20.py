def main():
    lista_pitagorica=[[i*j for i in range (1,11)] for j in range(1,11)]
    print("lista pitagorica: ")
    ##print(lista_pitagorica)
    for k,tabellina in enumerate(lista_pitagorica): ##ritorna l'indice della lista e il suo elemento
        print(f"tabellina del {k+1}: {tabellina}")
    file = open("lista_pitagorica.txt", "w")
    file.write("ma ciao giorgis \n")
    for i in lista_pitagorica:
        file.write(f"{i}\n")

    ##with open("lista_pitagorica.txt", "w") as fp:
      ##  for i in lista_pitagorica:
        ##    fp.write(str(i)+ " ")
    file.close()
if __name__ == "__main__":
    main()