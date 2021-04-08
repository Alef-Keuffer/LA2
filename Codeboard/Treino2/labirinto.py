'''13
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''

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
        if (x, y) == (s - 1, s - 1):
            mark.append(prev)
            return
        if (x, y) not in c:
            if mapa[x][y] == ' ':
                c.add((x, y))
                call_army_caminho(mapa, x, y, s, c, prev, mark)