def main():
    parola="ciao come stai?"
    parola_consonanti="".join([c for c in parola if c not in "aeiou"])
    print(parola)
    print(parola_consonanti)
if __name__ == "__main__":
    main()