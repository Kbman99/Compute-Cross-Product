class Vectors1:
    def __init__(self, v1, v2, cp=None):
        self.id = 0
        self.vector1 = self.set_values(v1)
        self.vector2 = self.set_values(v2)
        if not cp:
            self.result = [VectorValue(v) for v in self.calc_cp(v1, v2)]
        else:
            self.result = self.set_values(cp)
        self.created = 0

    def calc_cp(self, v1, v2):
        if not any(not isinstance(x, (str, float)) for x in v1 + v2):
            raise TypeError
        return [v1[1] * v2[2] - v1[2] * v2[1],
                v1[2] * v2[0] - v1[0] * v2[2],
                v1[0] * v2[1] - v1[1] * v2[0]]

    def set_values(self, values):
        vector = [VectorValue(v) for v in values]
        if len(vector) != 3:
            raise ValueError('size')
        else:
            return vector


class VectorValue:
    def __init__(self, val):
        self.val = val


class AllVectors:
    def __init__(self):
        self.results = []


class Vectors:
    def __init__(self, v1, v2, result=None):
        self.vector1 = v1
        self.vector2 = v2
        self.result = result if result else self.calc_cp()

    def calc_cp(self):
        return [self.vector1[1] * self.vector2[2] - self.vector1[2] * self.vector2[1],
                self.vector1[2] * self.vector2[0] - self.vector1[0] * self.vector2[2],
                self.vector1[0] * self.vector2[1] - self.vector1[1] * self.vector2[0]]
