def main():

    ip = "192.168.0.1"
    groups = ip.split('.')
    groups = [int(groups) for groups in groups]
    print(groups)
    groups_bin = [bin(group) for group in groups] ## mi stampa 0b all'inizio e per 0 e 1 non lo fa in ottetti
    print(groups_bin)

if __name__ == "__main__":
    main()