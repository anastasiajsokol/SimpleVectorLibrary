def stupid_sqrt(x, eps = 0.01):
    if(x < eps):
        return x
    def make_guess(x):
        digits = len(str(int(x)))
        half = digits / 2 + 0 if digits % 2 == 0 else 1
        guess_2 = 2 * 10 ** (half - 1)
        guess_7 = 7 * 10 ** (half - 1)
        return guess_2 if abs(guess_2 - x) < abs(guess_7 - x) else guess_7
    guess = make_guess(x)
    old_guess = 0
    while abs(guess - old_guess) > eps:
        old_guess = guess
        guess = (old_guess + x / old_guess) / 2
    return guess

sqrt = stupid_sqrt # set to actual sqrt function, please

class Vector:
    __slots__ = ["data"]

    def __init__(self, data):
        if(type(data) == list):
            self.data = data
        elif(hasattr(data, "__iter__") or hasattr(data, "__next__")):
            self.data = list(data)
        else:
            raise ValueError(f"Passed invalid type to Vector() | Passed: '{data}' type = {type(data)}")

    def dot(self, other):
        return sum((a * b for a, b in zip(self.data, other)))
    
    def cross(self, v):
        u = self.data
        if(len(u) != 3 or len(v) != 3):
            raise ValueError("Cross product only defined for 3d vectors")
        return [v[1] * u[2] - v[2] * u[1],
                v[2] * u[0] - v[0] * u[2],
                v[0] * u[1] - v[1] * u[0]]


    def __iadd__(self, other):
        if(len(other) != len(self.data)):
            raise ValueError(f"Can not add Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
        data = self.data
        for i, v in enumerate(other):
            data[i] += v
        return self

    def __add__(self, other):
        if(len(other) != len(self.data)):
            raise ValueError(f"Can not add Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
        temp = Vector(self.data.copy())
        tdata = temp.data
        for i, v in enumerate(other):
            tdata[i] += v
        return temp
    
    def __isub__(self, other):
        if(len(other) != len(self.data)):
            raise ValueError(f"Can not subtract Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
        data = self.data
        for i, v in enumerate(other):
            data[i] -= v
        return self
    
    def __sub__(self, other):
        if(len(other) != len(self.data)):
            raise ValueError(f"Can not subtract Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
        temp = Vector(self.data.copy())
        tdata = temp.data
        for i, v in enumerate(other):
            tdata[i] -= v
        return self
    
    def __imul__(self, other):
        if(type(other) == int or type(other) == float):
            data = self.data
            for i in range(len(data)):
                data[i] *= other
        else:
            if(len(other) != len(self.data)):
                raise ValueError(f"Can not multiply Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
            for i, v in enumerate(other):
                data[i] *= v
        return self

    def __mul__(self, other):
        temp = Vector(self.data.copy())
        tdata = temp.data
        if(type(other) == int or type(other) == float):
            for i in range(len(tdata)):
                tdata[i] *= other
        else:
            if(len(other) != len(self.data)):
                raise ValueError(f"Can not multiply Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
            for i, v in enumerate(other):
                tdata[i] *= v
        return temp

    def __itruediv__(self, other):
        data = self.data
        if(type(other) == int or type(other) == float):
            for i in range(len(data)):
                data[i] /= other
        else:
            if(len(other) != len(self.data)):
                raise ValueError(f"Can not divide Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
            for i, v in enumerate(other):
                data[i] /= v
        return self
    
    def __truediv__(self, other):
        temp = Vector(self.data.copy())
        tdata = temp.data
        if(type(other) == int or type(other) == float):
            for i in range(len(tdata)):
                tdata[i] /= other
        else:
            if(len(other) != len(self.data)):
                raise ValueError(f"Can not divide Vectors of with different dimensions | Vector(len = {len(self.data)}) v. Vector(len = {len(other)})")
            for i, v in enumerate(other):
                tdata[i] /= v
        return temp

    def __getitem__(self, idx):
        return self.data[idx]
    
    def __setitem__(self, idx, val):
        self.data[idx] = val
    
    def __abs__(self):
        return sqrt(sum((x ** 2 for x in self.data)))

    def __iter__(self):
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return "Vector(" + ', '.join((str(x) for x in self)) + ")"
    
    def __repr__(self):
        return str(self)
