from Codeboard.support import dijkstra, build, dijkstra_all_paths

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
    return saltos_rec(sorted(map(abs, (o[0] - d[0], o[1] - d[1]))))


def saltos_rec(x):
    p = sorted(map(abs, x))
    return 3 * (p[0] + p[1]) % 4 if (p[0] and p[1]) < 3 else 1 + saltos_rec((p[0] - 1, p[1] - 2))


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


# %%
def tamanho(ruas):
    edges = [(r[0], r[-1], len(r)) for r in ruas]
    vertices = {x[0] for x in ruas}.union({x[-1] for x in ruas})
    dis = dijkstra_all_paths(build(edges), vertices)
    return max([x[1] for r in dis for x in r.items()])
