class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, coord_2):
        x_diff = (self.x - coord_2.x)**2
        y_diff = (self.y - coord_2.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    # print(isinstance(coord_2, Coordenada))
