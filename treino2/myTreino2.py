from math import ceil

'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical.

'''


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
