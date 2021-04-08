'''13
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical.
'''

def area(p, mapa1):
    class GridWithWeights:
        # Adapted from https://www.redblobgames.com/pathfinding/a-star/
        def neighbors(self, grid_loc):
            (x, y) = grid_loc
            neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
            results = filter(self.in_bounds, neighbors)
            results = filter(self.passable, results)
            return results

        def cost(self, from_node, _):
            return 1

        def __init__(self, mapa, wall_symbol):
            self.width = len(mapa[0])
            self.height = len(mapa)
            self.walls = [(x, y)
                          for x in range(self.width)
                          for y in range(self.height)
                          if mapa[y][x] == wall_symbol]

        def in_bounds(self, grid_loc):
            (x, y) = grid_loc
            return 0 <= x < self.width and 0 <= y < self.height

        def passable(self, grid_loc):
            return grid_loc not in self.walls

    def breadth_first_search(graph, start):
        # Used from https://www.redblobgames.com/pathfinding/a-star/
        from collections import deque
        frontier = deque()
        frontier.append(start)
        came_from = {start: None}

        while frontier:
            current = frontier.popleft()

            for NEXT in graph.neighbors(current):
                if NEXT not in came_from:
                    frontier.append(NEXT)
                    came_from[NEXT] = current
        return came_from

    g = GridWithWeights(mapa1, '*')
    return len(breadth_first_search(g, p))
