''' 13
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul.O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.
'''


def travessia(mapa):
    # Strategy: Shortest path from edges filled with 0
    g = GridWithWeights(len(mapa[0]), len(mapa))
    g.weights = {(x, y): int(mapa[y][x])
                 for x in range(g.width)
                 for y in range(g.height)}
    start = -1, -1
    goal = -2, -2
    return dijkstra_search(g, start, goal)


class GridWithWeights:
    # Adapted from https://www.redblobgames.com/pathfinding/a-star/
    def neighbors(self, grid_loc):
        (x, y) = grid_loc
        if grid_loc == (-1, -1):
            return [(x_c, 0) for x_c in range(self.width)]
        elif grid_loc[1] == self.height - 1:
            return [(-2, -2)]
        else:
            neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]

            def passable(loc):
                return self.sub1(grid_loc, loc) <= 2

            results = filter(self.in_bounds, neighbors)
            results = filter(passable, results)
            return results

    def sub1(self, loc1, loc2):
        return abs(self.weights[loc1] - self.weights[loc2])

    def in_bounds(self, grid_loc):
        (x, y) = grid_loc
        return 0 <= x < self.width and 0 <= y < self.height

    def cost(self, from_node, to_node):
        if from_node == (-1, -1) or to_node == (-2, -2):
            return 0
        else:
            return 1 + self.sub1(from_node, to_node)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.weights = {}


def dijkstra_search(graph, start, goal):
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
                priority = new_cost
                push(hq, (priority, NEXT))
                came_from[NEXT] = current

    # pi = reconstruct_path(came_from, start, goal)
    # return cost_so_far[goal]
    return reconstruct_path(came_from, start, goal)[1][0], cost_so_far[goal]


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
