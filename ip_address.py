import ipaddress

#se privato o loopback
#se indirizzo rete valido, se si stampa tutti gli ip utilizzabili 

def main():
    ip=input("Inserisci un indirizzo: ")
    mask=input("Inserisci la sua subnet mask (con /): ")
    istanza_ip=ipaddress.IPv4Address(ip)
    ip_2=ip+mask
    if istanza_ip.is_private:
        print("E' privato!")
    if istanza_ip.is_loopback:
        print("E' di loopback!") 
    ip_rete=ipaddress.IPv4Network(ip_2,strict=False) #strict sempre a false se non è ip di rete, con false lo calcola
    if ip_2 == str(ip_rete): #con str si genera una stringa e la confronta con ip
        print("E' di rete!")
    else:
        print("Non è di rete!")
    print(f"indirizzo di rete: {ip_rete}")
    host = list(ip_rete.hosts()) 
    print(f"Il primo ip utilizzabile è: {host[0]}")
    print(f"L'ultimo ip utilizzabile è: {host[-1]}")   

if __name__ == "__main__":
    main()