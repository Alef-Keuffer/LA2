'''12
Podemos usar um (multi) grafo para representar um mapa de uma cidade:
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que calcula o tamanho de uma cidade,
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a
letras do alfabeto, e cada rua começa (e acaba) no cruzamento
identificado pelo primeiro (e último) caracter do respectivo nome.

'''


def tamanho(ruas):
    ruas1 = [(r[0], r[-1], len(min(ruas, key=lambda x: len(x) if x[0] == r[0] and x[-1] == r[-1] else float('inf'))))
             for r in ruas]
    ruas2 = {x[0] for x in ruas}.union({x[-1] for x in ruas})
    dis = [dijkstra(build(ruas1), o)[0] for o in ruas2]
    return max([x[1] for r in dis for x in r.items()])


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