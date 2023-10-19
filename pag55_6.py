def main():
    s="ciao"
    print(s)
    print("stampa caratteri con indice dispari:")
    for i in range(len(s)):
        if i%2!=0:
            print(s[i])
            
if __name__ == "__main__":
    main()