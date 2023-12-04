def main():
    ip_addresses=["192.168.222.0/27","192.168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    with open("mask.txt","w") as file:
        for ip_address in ip_addresses:
            ip, mask = ip_address.split('/')
            mask_int = int(mask)
            sm = '1' * mask_int + '0' * (32-mask_int)
            print('.'.join([sm[i:i+8]for i in range(0,32,8)]))
            sm = sm[:8] + '.' + sm[8:16] + '.' + sm[16:24] + '.' + sm[24:]
            file.write(f"{ip} - mask({mask}): {sm} \n")

if __name__ == "__main__":
    main()