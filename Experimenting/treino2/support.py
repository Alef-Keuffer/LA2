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


def gen_pi(x, t):
    ka = []
    if t in x:
        ka = [x[t]]
        while ka[-1] in x:
            ka.append(x[ka[-1]])
    return ka


def gen_pi_forward(x):
    ka = [x.get(list(x.values())[0]), x.get(list(x.keys())[0])]
    while ka[-1] in x:
        ka.append(x[ka[-1]])
    return ka


def dfs(adj, o):
    return dfs_aux(adj, o, [], {})


def dfs_aux(adj, o, vis, pi):
    vis.insert(0, o)
    for d in adj.get(o, []):
        if d not in vis:
            pi[d] = o
            dfs_aux(adj, d, vis, pi)
    return pi, vis
