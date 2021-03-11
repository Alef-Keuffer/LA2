# nextLan2 :: Int -> [Lan a]
def next_lan(n):
    s = {'a'}
    next_lan_rec(n, 'a', s)
    # re = sorted(s)
    # re.sort(key=lambda x: len(x))
    return s


# %% code
print('Hello World')


def next_lan_rec(n, x, s):
    if n > 0:
        s.add('b' + x)
        s.add(x + 'b')
        next_lan_rec(n - 1, 'b' + x, s)
        next_lan_rec(n - 1, x + 'b', s)


def next_lan2(n: int) -> list:
    s = set()
    next_lan_rec2(n, 'a', s)
    re = sorted(s)
    re.sort(key=lambda x: len(x))
    return re


def next_lan_rec2(n, x, s):
    s.add(x)
    next_lan_left(n - 1, x, s)
    next_lan_right(n - 1, x, s)
    return s


def next_lan_left(n, x, s):
    if n >= 0:
        s.add('b' + x)
        next_lan_left(n - 1, 'b' + x, s)


def next_lan_right(n, x, s):
    if n >= 0:
        s.add(x + 'b')
        next_lan_right(n - 1, x + 'b', s)




"""def Dijkstra(Graph, source,target):
  Q = set()
  dist = {}
  prev = {}
  for v in Graph:
      dist[v] = -1
      prev[v] = -1
  dist[source] = 0
  u = target
  while Q:
      u = min Q
      Q.remove(u)
  if prev[u] is defined or u = source:          # Do something only if the vertex is reachable
      while u is defined:                       # Construct the shortest path with a stack S
          insert u at the beginning of S        # Push the vertex onto the stack
          u ← prev[u]                           # Traverse from target to source
          u ← prev[u]      """  # Traverse from target to source
