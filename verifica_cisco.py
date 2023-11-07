def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return ("0"*(8-l) + b)
def conversioneDecimale(ip_binario):
    gruppiDecimali=[]
    for i in range(0,32,8):
        ottetto=ip_binario[i:i+8]
        gruppiDecimali.append(str(int(ottetto,2)))
    return ".".join(gruppiDecimali)
        
def main():

    ipAddress = input("inserisci indirizzo ip: ")
    sub_num = int(input("inserisci subnet mask in CIDR: "))
    sub_bin = "1"*sub_num + "0"*(32 - sub_num)
    wild_bin = "0"*sub_num + "1"*(32 - sub_num)
    groups = ipAddress.split(".")
    groups = [int(group) for group in groups]
    groups_b = [bin(elemento) for elemento in groups]
    groups_strbin = [completa8bit(strbin) for strbin in groups_b]
    ipAddress_bin = "".join(groups_strbin)
    rete_str = ["1" if (a == "1" and b == "1") else "0" for a, b in zip(ipAddress_bin, sub_bin)]
    broad_str = ["1" if (a == "1" or b == "1") else "0" for a, b in zip(ipAddress_bin, wild_bin)]
    rete_bin = "".join(rete_str)
    broad_bin = "".join(broad_str)
    list_rete_bin = [rete_bin[i:i+8] for i in range(0, 32, 8)]
    list_broad_bin = [broad_bin[i:i+8] for i in range(0, 32, 8)]
    list_rete_dec = [int(group, 2) for group in list_rete_bin]
    list_broad_dec = [int(group, 2) for group in list_broad_bin]
    print(f"rete: {list_rete_dec}")
    print(f"broadcast: {list_broad_dec}")
if __name__ == "__main__":
    main()