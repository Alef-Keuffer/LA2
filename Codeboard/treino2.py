"""
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical.
"""


def call_army(mapa, x, y, s, c):
    rob(mapa, x + 1, y, s, c)
    rob(mapa, x - 1, y, s, c)
    rob(mapa, x, y - 1, s, c)
    rob(mapa, x, y + 1, s, c)


def rob(mapa, x, y, s, c):
    if x in range(s) and y in range(s):
        if (x, y) not in c:
            if mapa[x][y] == '.':
                c.add((x, y))
                call_army(mapa, x, y, s, c)


def area(p, mapa):
    aval = set()
    rob(mapa, p[0], p[1], len(mapa), aval)
    return len(aval)


"""
O objectivo deste problema é determinar quantos movimentos são necessários para
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.
"""


def saltos_rec(x):
    p = sorted(map(abs, x))
    if (p[0] and p[1]) < 3:
        return 3 * (p[0] + p[1]) % 4
    return 1 + saltos_rec((p[0] - 1, p[1] - 2))


def saltos(o, d):
    p = sorted(map(abs, (o[0] - d[0], o[1] - d[1])))
    return saltos_rec(p)


"""
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
"""


def viagem(rotas, source, target):
    adj = build([(r[i], r[i + 2], r[i + 1]) for r in rotas for i in range(len(r) - 1) if i % 2 == 0])
    return dijkstra(adj, source, target)


def dijkstra(adj, o, target=None):
    pi = {}
    dist = {o: 0}
    Q = {o}
    while Q:
        v = min(Q, key=lambda x: dist[x])
        Q.remove(v)
        if target is not None:
            if v == target:
                break
        for d in adj[v]:
            if d not in dist:
                Q.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pi[d] = v
                dist[d] = dist[v] + adj[v][d]
    if target is not None:
        return dist[target]
    return dist, pi


def build(edges, adj=None):
    # Assumes edges :: [(v,v,weight::int)]
    if adj is None:
        adj = {}
    for o, d, p in edges:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = p
        adj[d][o] = p
    return adj
