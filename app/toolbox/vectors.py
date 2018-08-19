class Vectors:
    def __init__(self, v1, v2, result=None):
        self.vector1 = v1
        self.vector2 = v2
        self.result = result if result else self.calc_cp()

    def calc_cp(self):
        return [self.vector1[1] * self.vector2[2] - self.vector1[2] * self.vector2[1],
                self.vector1[2] * self.vector2[0] - self.vector1[0] * self.vector2[2],
                self.vector1[0] * self.vector2[1] - self.vector1[1] * self.vector2[0]]


class AllVectors:
    def __init__(self):
        self.results = []
