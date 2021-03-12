def dijkstra_all_paths(adj, vertices):
    return [dijkstra(adj, v)[0] for v in vertices]


# must build dijsktra directed

def dijkstra(adj, o, target=None):
    pi = {}
    dist = {o: 0}
    Q = {o}
    while Q:
        v = min(Q, key=lambda x: dist.get(x, []))
        Q.remove(v)
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


def build(edges, adj=None):
    # Assumes edges :: [(v,v,weight::int)]
    edges = [(r[0], r[1], min(edges, key=lambda x: x[2] if x[0] == r[0] and x[1] == r[1] else float('inf'))[2])
             for r in edges]  # Should allow me to deal with multigraphs
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


def gen(x, t):
    ka = []
    if t in x:
        ka = [x[t]]
        while ka[-1] in x:
            ka.append(x[ka[-1]])
    return ka
