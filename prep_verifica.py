lettere = "abcdefghilmnopqrstuvz ?"
N = len(lettere)
lettere2numeri = {}
numeri2lettere = {}
for posizione, lettera in enumerate(lettere):
    lettere2numeri[lettera]= posizione
    numeri2lettere[posizione]= lettera
    
testo_chiaro = "ciao come stai?"
chiave = "itisdelpozzo fprfrncnc rnfrfrovmc rmfcpdndpcs?"
testo_criptato = ""
testo_chiaro2 = ""

for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave):
    numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave])%N
    testo_criptato += numeri2lettere[numero]
print(f"il testo in chiaro '{testo_chiaro}' diventa: '{testo_criptato}'")


for lettera_testo, lettera_chiave in zip(testo_criptato, chiave):
    numero = (lettere2numeri[lettera_testo] - lettere2numeri[lettera_chiave])%N
    testo_chiaro2 = testo_chiaro2 + numeri2lettere[numero]
print(f"il testo criptato '{testo_criptato}' diventa: '{testo_chiaro2}'")