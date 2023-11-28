def main():
    nome=input("Inserisci un nome: ")
    print(f"nome base: {nome}")
    nome_2=nome[0]+ "*" * (len(nome)-1)
    print(f"nome modificato: {nome_2}")
if __name__ == "__main__":
    main()