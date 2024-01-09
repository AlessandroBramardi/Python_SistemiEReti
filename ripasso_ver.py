dizionario = {"a":"alberto", "b": "brutto", "c": "cane"}
lista = ["alberto","brutto","cane"]
print(dizionario["b"])
print(lista[1])
dizionario["d"] = "dado"
dizionario["a"] = "alto"
print(dizionario)

for chiave in dizionario:
    print(f"la chiave: {chiave} -> {dizionario[chiave]}")
    
if "a" in dizionario:
    print("a è nel dizionario")