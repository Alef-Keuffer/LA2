'''13
O objectivo deste problema é determinar quantos movimentos são necessários para
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.
'''


def saltos(o, d):
    class Graph:
        def cost(self, _, __):
            return 1

        moves = [(-2, -1), (1, 2), (-2, 1), (1, -2),
                 (-1, -2), (2, 1), (-1, 2), (2, -1)]

        def neighbors(self, loc):
            return [adt(loc, x) for x in self.moves]

    def adt(t1, t2):
        return tuple(x + y for x, y in zip(t1, t2))

    def dijkstra_search(graph, start, goal, heuristic=lambda x, y: 0):
        # Adapted from https://www.redblobgames.com/pathfinding/a-star/
        from heapq import heappush as push, heappop as pop
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
                    priority = new_cost + heuristic(NEXT, goal)
                    push(hq, (priority, NEXT))
                    came_from[NEXT] = current

        # pi = reconstruct_path(came_from, start, goal)
        return cost_so_far[goal]

    def heuristic1(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    g = Graph()
    return dijkstra_search(g, o, d, heuristic1)


# Não consegui usar essa função abaixo
def saltos2(o, d):
    if o == d:
        return 0
    return saltos_rec(sorted(map(abs, (o[0] - d[0], o[1] - d[1]))))


def saltos_rec(x):
    p = sorted(map(abs, x))
    return 3 * (p[0] + p[1]) % 4 if (p[0] < 3 and p[1] < 3) else 1 + saltos_rec((p[0] - 1, p[1] - 2))
