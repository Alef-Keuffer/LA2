'''13
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra.
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si.
A função deverá devolver o tamanho do maior continente.
'''
def maior(neigh1):
    # Transform continents into sets
    neigh = [set(x) for x in neigh1]

    def red(x, lis):
        a = x.copy()
        li = lis.copy()
        for e in lis:
            if a.intersection(e) != set():
                li.remove(e)
                a = a.union(e)
        li.append(a)
        return li

    for x in neigh:
        neigh = red(x, neigh)
    return max(len(x) for x in neigh) if neigh else 0