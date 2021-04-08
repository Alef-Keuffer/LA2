'''13
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
'''


def viagem(rotas, source, target):
    adj = build([(r[i], r[i + 2], r[i + 1]) for r in rotas for i in range(len(r) - 1) if i % 2 == 0])
    return dijkstra(adj, source, target)[0]


def dijkstra(adj, o, target=None):
    pi = {}
    dist = {o: 0}
    Q = {o}
    while Q:
        v = min(Q, key=lambda x: dist.get(x, []))
        Q.remove(v)
        if target is not None:
            if v == target:
                break
        for d in adj.get(v, []):
            if d not in dist:
                Q.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pi[d] = v
                dist[d] = dist[v] + adj[v][d]
    if target is not None:
        return dist.get(target, float('inf')), pi.get(target)
    return dist, pi


def undirected(t):
    return t + [(r[1], r[0], r[2]) for r in t]


def build(edges, adj=None, opt1='undi'):
    # Assumes edges :: [(v,v,weight::int)]
    if opt1 == 'dir':
        edges1 = [(r[0], r[1], min(edges, key=lambda x: x[2] if x[0] == r[0] and x[1] == r[1] else float('inf'))[2])
                  for r in edges]
    else:
        dual = undirected(edges)
        edges1 = [(r[0], r[1], min(dual, key=lambda x: x[2] if x[0] == r[0] and x[1] == r[1] else float('inf'))[2])
                  for r in dual]
    if adj is None:
        adj = {}
    for o, d, p in edges1:
        if o not in adj:
            adj[o] = {}
        adj[o][d] = p
    return adj


"""

def viagem(rotas, source, target):
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
