from Experimenting.treino2.support import *

"""
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical.
"""


def area(p, mapa):
    aval = set()
    rob(mapa, p[0], p[1], len(mapa), aval)
    return len(aval)


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


"""
O objectivo deste problema é determinar quantos movimentos são necessários para
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.
"""


def saltos(o, d):
    if o == d:
        return 0
    return saltos_rec(sorted(map(abs, (o[0] - d[0], o[1] - d[1]))))


def saltos_rec(x):
    p = sorted(map(abs, x))
    return 3 * (p[0] + p[1]) % 4 if (p[0] < 3 and p[1] < 3) else 1 + saltos_rec((p[0] - 1, p[1] - 2))


"""
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
"""


def viagem(rotas, source, target):
    adj = build([(r[i], r[i + 2], r[i + 1]) for r in rotas for i in range(len(r) - 1) if i % 2 == 0])
    return dijkstra(adj, source, target)[0]


def tamanho(ruas):
    edges = [(r[0], r[-1], len(r)) for r in ruas]
    vertices = {x[0] for x in ruas}.union({x[-1] for x in ruas})
    dis = dijkstra_all_paths(build(edges), vertices)
    return max([x[1] for r in dis for x in r.items()])


"""
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

    inp1 = [["Portugal", "Espanha"], ["Espanha", "França"], ["França", "Bélgica", "Alemanha", "Luxemburgo"],
            ["Canada", "Estados Unidos"]]
    inp2 = [["Portugal", "Espanha"], ["Espanha", "França"]]
    assert maior(inp1) == 6
    assert maior(inp2) == 3

"""


def maior(neigh):
    ra = [(x[i - 1], x[i], 0) for x in neigh for i in range(0, len(x))]
    re = [dfs(build(ra), y)[1] for y in set([k for z in neigh for k in z])]
    re.append([])
    return max(map(len, re))


"""
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.
"""


def erdos(art, limit):
    art1 = [x for x in art.values()]
    en = {'Paul Erdos': 0}
    s = {'Paul Erdos'}
    b = next(filter(lambda x: x.intersection(s) != set() and x.intersection(s) != x, art1), None)
    while b:
        for a in b:
            if a not in s:
                en[a] = en[min(b, key=lambda x: en.get(x, float('inf')))] + 1
                s.add(a)
        b = next(filter(lambda x: x.intersection(s) != set() and x.intersection(s) != x, art1), None)
    return sorted(sorted(list(filter(lambda x: en[x] <= limit, en.keys())), key=lambda x: str.lower(x)),
                  key=lambda x: en[x])


"""
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.
"""


def caminho(mapa):
    aval = set()
    p = (0, 0)
    mark = ['']
    rob_caminho(mapa, p[0], p[1], len(mapa), aval, '', mark)
    return mark[-1]


def call_army_caminho(mapa, x, y, s, c, prev, mark):
    rob_caminho(mapa, x + 1, y, s, c, prev + 'S', mark),
    rob_caminho(mapa, x - 1, y, s, c, prev + 'N', mark),
    rob_caminho(mapa, x, y - 1, s, c, prev + 'O', mark),
    rob_caminho(mapa, x, y + 1, s, c, prev + 'E', mark)


def rob_caminho(mapa, x, y, s, c, prev, mark):
    if x in range(s) and y in range(s):
        if (x, y) not in c:
            if mapa[x][y] == ' ':
                if (x, y) == (s - 1, s - 1):
                    mark.append(prev)
                    return
                c.add((x, y))
                call_army_caminho(mapa, x, y, s, c, prev, mark)


"""def travessia(mapa):
    var1 = [caminho_travessia((x, 0), mapa) for x in range(len(mapa[0]))]
    ret = min(var1, key=lambda x: list_of_cord_to_weight(mapa, x))
    ret.sort(key=lambda x: x[0][0])
    return ret[0]


def caminho_travessia(p, mapa):
    aval = set()
    mark = [p]
    rob_travessia(mapa, p[0], p[1], [len(mapa), len(mapa[0])], aval, [p], mark)
    ret = min(mark, key=lambda x: list_of_cord_to_weight(mapa, x))
    ret.sort(key=lambda x: x[0][0])
    return ret[0]


def cord_to_value(mapa, c):
    return mapa[c[0]][c[1]]


def weight_list_to_weight(li):
    return sum([abs(li[i] - li[i + 1]) + 1 for i in range(len(li) - 1)])


def list_of_cord_to_weight(mapa, la):
    return weight_list_to_weight([cord_to_value(mapa, c) for c in la])


def call_army_travessia(mapa, x, y, s, c, prev, mark):
    rob_travessia(mapa, x + 1, y, s, c, prev, mark),
    rob_travessia(mapa, x - 1, y, s, c, prev, mark),
    rob_travessia(mapa, x, y - 1, s, c, prev, mark),
    rob_travessia(mapa, x, y + 1, s, c, prev, mark)


def rob_travessia(mapa, x, y, s, c, prev, mark):
    if x in range(s[0]) and y in range(s[1]):
        if (x, y) not in c:
            if int(mapa[x][y]) - int(mapa[prev[-1][0]][prev[-1][1]]) <= 2:
                if y == s[1]:
                    mark.append(prev)
                    return
                c.add((x, y))
                prev.append((x, y))
                call_army_travessia(mapa, x, y, s, c, prev, mark)
"""


def travessia(mapa0):
    # Strategy: Shortest path from a node that
    # can go to all starting nodes for free
    # to node after ending line but where the cost to move
    # in x axis is free
    nil = ''.join('0' for _ in range(len(mapa0[0])))
    mapa = mapa0 + [nil]
    mapa.insert(0, nil)
    g = GridWithWeights(len(mapa[0]), len(mapa))
    g.weights = {(x, y): int(mapa[y][x])
                 for x in range(g.width)
                 for y in range(g.height)}
    start, goal = (0, 0), (0, g.height - 1)
    came_from, cost_so_far = dijkstra_search(g, start, goal)
    # Find which node I actually started
    rx = [x for x in reconstruct_path(came_from, start, goal) if x[1] != 0][0][0]
    # Get cost of the trip
    rc = cost_so_far[goal]
    return rx, rc


class GridWithWeights:
    # Used code from https://www.redblobgames.com/pathfinding/a-star/
    # Adapted cost function
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.weights = {}

    def in_bounds(self, grid_loc):
        (x, y) = grid_loc
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, grid_loc):
        x, y = grid_loc
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # E W N S
        return filter(self.in_bounds, neighbors)

    def cost(self, from_node, to_node):
        if from_node[1] == 0:
            return 0
        elif to_node[1] == self.height - 1:
            return 0
        dif = abs(self.weights.get(to_node, 1) - self.weights.get(from_node, 1))
        if dif <= 2:
            return dif + 1
        else:
            return float('inf')


def dijkstra_search(graph, start, goal):
    from _heapq import heappush as push, heappop as pop
    hq = []  # heap queue
    push(hq, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while hq:
        current = pop(hq)[1]

        if current == goal:
            break

        for NEXT in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, NEXT)
            if NEXT not in cost_so_far or new_cost < cost_so_far[NEXT]:
                cost_so_far[NEXT] = new_cost
                priority = new_cost
                push(hq, (priority, NEXT))
                came_from[NEXT] = current

    return came_from, cost_so_far


def reconstruct_path(came_from, start, goal):
    # Used code from https://www.redblobgames.com/pathfinding/a-star/
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
