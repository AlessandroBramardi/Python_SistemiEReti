def contaNucleotidi(stringa):
    a,c,g,t= 0,0,0,0
    for char in stringa:
        if char == "C":
            c+=1
        elif char == "A":
            a+=1
        elif char == "G":
            g+=1
        elif char == "T":
            t+=1
    return a,c,g,t

def contaNucleotidi2(stringa):
    dizNucleoditi={"A": 0, "C":0,"G":0,"T":0}
    for char in stringa:
        dizNucleoditi[char] = dizNucleoditi[char]+1
    return dizNucleoditi
def contaNucleotidi3(stringa, nucleotide):
    return len([x for x in stringa if x == nucleotide ])

def cercaProteinaSpike(stringa):
    proteinaSpike = "ATGTTTGTTTT"
    for i, _ in enumerate(stringa[:-12]):
        if stringa[i:i+len(proteinaSpike)] == proteinaSpike:
            return i
    return -1

def main():
    file = open("covid-19.txt","r")
    righe = file.readlines()
    file.close
    genoma = ""
    for riga in righe:
        genoma = genoma+riga[0:-1]
        genoma += riga
    a, c, g, t =  contaNucleotidi(genoma)

    print(f"A: {a}, C: {c}, G: {g}, T: {t}")
    print(contaNucleotidi2(genoma))
    posProtSpike = cercaProteinaSpike(genoma)
    print(posProtSpike)

if __name__ == "__main__":
    main()