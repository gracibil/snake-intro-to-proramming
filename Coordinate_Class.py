class Coordinate(object):
    height = 0
    width = 0

    def __init__(self, coord_x, coord_y):
        self.coord_x = int(coord_x)
        self.coord_y = int(coord_y)

    def add_coord_y(self):
        if self.coord_y == Coordinate.height - 1:
            self.coord_y = -1
        self.coord_y += 1

        return self.coord_x , self.coord_y

    def sub_coord_y(self):
        if self.coord_y == 0:
            self.coord_y = Coordinate.height - 1
        else:
            self.coord_y -= 1
        return self.coord_x, self.coord_y

    def add_coord_x(self):
        if self.coord_x == Coordinate.width-1:
            self.coord_x = 0
        else:
            self.coord_x += 1
        return self.coord_x, self.coord_y

    def sub_coord_x(self):
        if self.coord_x == 0:
            self.coord_x = Coordinate.width - 1
        else:
            self.coord_x -= 1
        return self.coord_x, self.coord_y