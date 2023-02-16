class CoordinateRow(object):
    def __init__(self):
        self.coordniate_row = [(0,0), (1,0)]

    def add_coordinate(self, coords):
        self.coordniate_row.append(coords)

    def remove_coordinate(self):
        removed = self.coordniate_row.pop(0)
        return removed

    def get_last_coord(self):
        coord = self.coordniate_row[len(self.coordniate_row)-1]
        return coord
