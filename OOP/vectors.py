class Vector3D():
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x**2 + y**2 + z**2)**0.5
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
    def __mul__(self, inst):
        if type(inst) == int:
            return Vector(inst * self.x, inst * self.y, inst * self.z)
        if type(inst) == float:
            return Vector(inst * self.x, inst * self.y, inst * self.z)
        else:
            x = self.x * inst.x
            y = self.y * inst.y
            z = self.z * inst.z
            return x + y + z
    def __rmul__(self, inst):
        if type(inst) == int:
            return Vector(inst * self.x, inst * self.y, inst * self.z)
        if type(inst) == float:
            return Vector(inst * self.x, inst * self.y, inst * self.z)
        else:
            x = self.x * inst.x
            y = self.y * inst.y
            z = self.z * inst.z
            return x + y + z
    def __matmul__(self, inst):
        x = self.y * inst.z - self.z * inst.y
        y = self.z * inst.x - self.x * inst.z
        z = self.x * inst.y - self.y * inst.x
        return Vector3D(x, y, z)
    def __sub__(self, inst):
        inst1 = (-1) * inst
        return(self + inst1)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

vec1 = Vector3D(1, 0, 0)
vec2 = Vector3D(5, 9, 0)
vec3 = vec1 - vec2
vec4 = vec1 * vec3
vec5 = vec2@(vec3@vec1)
print(vec3)
print(vec4)
print(vec5)
print(vec1.length)
