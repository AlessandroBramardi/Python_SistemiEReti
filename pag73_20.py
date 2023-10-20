def main():
    lista_pitagorica=[i*j for i in range (1,11) for j in range(1,11)]
    print("lista pitagorica: ")
    print(lista_pitagorica)
    with open("lista_pitagorica.txt", "w") as fp:
        for i in lista_pitagorica:
            fp.write(str(i)+ " ")
if __name__ == "__main__":
    main()