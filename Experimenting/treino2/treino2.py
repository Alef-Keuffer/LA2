from math import ceil


'''

O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''


def fix_vec2(o, d):
    o1 = (max(o[0], o[1]), min(o[0], o[1]))
    o2 = (max(d[0], d[1]), min(d[0], d[1]))
    return abs(o1[0] - o2[0]), abs(o1[1] - o2[1])


def fix_vec(o, d):
    return sorted(map(abs, (o[0] - d[0], o[1] - d[1])), reverse=True)


def saltos_rec(x):
    if x == (0, 0):
        return 0
    p = fix_vec((0, 0), x)
    r = (p[0] % 3, p[1] % 3)
    re = 2 * (p[1] // 3)
    if r in {(1, 2), (2, 1)}:
        return re + 1
    elif r in {(1, 1)}:
        return re + 2
    elif r in {(1, 0), (0, 1)}:
        return re + 3
    else:
        return re + 1 + saltos_rec((p[0] - 2, p[1] - 1))


def saltos_exp_rec(x):
    p = sorted(map(abs, x), reverse=True)
    if (p[0] and p[1]) < 3:
        return 3 * (p[0] + p[1]) % 4
    return 1 + saltos_exp_rec((p[0] - 2, p[1] - 1))


def saltos_exp(o, d):
    p = sorted(map(abs, (o[0] - d[0], o[1] - d[1])), reverse=True)
    return saltos_exp_rec(p)


def saltos(o, d):
    # diagonal is 2 moves
    # x,y axis is 3 moves
    p = fix_vec(o, d)
    return saltos_rec(p)


"""
def viagem_v2(rotas, source, target):
    length = {}
    C = set()
    Adj = {}
    for l in rotas:
        i = 0
        while i in range(len(l) - 1):
            if (l[i], l[i + 2]) not in length:
                length[l[i], l[i + 2]] = l[i + 1]
                Adj[l[i]] = {l[i + 2]}
            if (l[i + 2], l[i]) not in length:
                length[l[i + 2], l[i]] = l[i + 1]
                Adj[l[i + 2]] = {l[i]}
            length[l[i], l[i + 2]] = min(length[l[i], l[i + 2]], l[i + 1])
            length[l[i + 2], l[i]] = min(length[l[i + 2], l[i]], l[i + 1])
            C.add(l[i])
            C.add(l[i + 2])
            i += 2
    return dijkstra_v2(C, length, source, target)

def dijkstra_v2(C, length, source, target):
    Q = set()
    dist = {}
    for v in C:
        dist[v] = float('inf')
        Q.add(v)
    dist[source] = 0
    while Q:
        u = min(Q, key=lambda x: dist[x])
        Q.remove(u)
        if u == target:
            break
        for v in [x for x in Q if (x, u) in length or (u, x) in length]:  # only v that are still in Q
            alt = dist[u] + length[u, v]
            if alt < dist[v]:
                dist[v] = alt
    return dist[target]
"""
