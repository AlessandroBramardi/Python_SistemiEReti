def main():
    s="ciao"
    print(s)
    print("stampa stringa eccetto prima e ultima lettera:")
    for i in range(len(s)):
        if s[i]!=s[0]:
            if s[i]!=s[-1]:
                print(s[i])


if __name__ == '__main__':
    main()