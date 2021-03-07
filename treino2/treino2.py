'''

O objectivo deste problema é determinar quantos movimentos são necessários para
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''


def saltos_rec(x):
    p = sorted(map(abs, x))
    if (p[0] and p[1]) < 3:
        return 3 * (p[0] + p[1]) % 4
    return 1 + saltos_rec((p[0] - 1, p[1] - 2))


def saltos(o, d):
    p = sorted(map(abs, (o[0] - d[0], o[1] - d[1])))
    return saltos_rec(p)
