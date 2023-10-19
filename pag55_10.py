def main():
    lista_voti=[7,4,3,5,9,8,6]
    print(lista_voti)
    print("Lista voti senza primo e ultimo voto:")
    for i in range(len(lista_voti)):
        if lista_voti[i]!=lista_voti[0]:
            if lista_voti[i]!=lista_voti[-1]:
                print(lista_voti[i])
    print("Quarto voto sostituito con un 10:")
    lista_voti[3]=10
    print(lista_voti)
    print("Primi 3 voti della lista:")
    for i in range(3):
        print(lista_voti[i])

if __name__ == '__main__':
    main()