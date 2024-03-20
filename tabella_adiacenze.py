import networkx as nx
import matplotlib.pyplot as plt #libreria per grafici

def prettyPrint(matrice, separatore):
    for riga in matrice:
        riga_str = [str(x) for x in riga]  # converto una lista in una lista di strighe
        print(separatore.join(riga_str))

def creaDiz(matrice, diz_inverso):
    diz_inverso = {i: [] for i in range(len(matrice))}
    for k in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[k][j] == 1:
                diz_inverso[k].append(j)
    print(diz_inverso)

def disegnaGrafo(dizionario):
    G = nx.Graph(dizionario)
    pos = nx.spring_layout(G)  # Layout del grafo
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=700, edge_color='gray')
    plt.show()

def main():
    matrice = []  # matrice quadrata vuota
    diz_r = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}  # dizionario per route
    diz_inverso = {}
    n = len(diz_r)
    matrice = [[0] * n for _ in range(n)]  # creo lista con n 0 dentro

    for k, v in diz_r.items():  # scorro sia chiave che valore
        for h in v:
            matrice[k][h] = 1

    prettyPrint(matrice, " ")
    creaDiz(matrice, diz_inverso)
    disegnaGrafo(diz_r)

if __name__ == '__main__':
    main()
