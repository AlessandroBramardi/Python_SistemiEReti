def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0"*(8-l)+b
    

def main():

    ip = "10.172.14.4"
    groups = ip.split('.')
    print (groups)
    groups = [int(group) for group in groups]
    print(groups)
    groups_bin = [bin(group) for group in groups] ## mi stampa 0b all'inizio e per 0 e 1 non lo fa in ottetti
    print(groups_bin)
    print(completa8bit(groups_bin[0]))
    groups_strbin = [completa8bit(strbin) for strbin in groups_bin]
    print(groups_strbin)
    print(".".join(groups_strbin))


if __name__ == "__main__":
    main()