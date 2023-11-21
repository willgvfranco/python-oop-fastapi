class Ponto:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}(x={self.x!r}, y={self.y!r})"


p1 = Ponto(1, 2)
p2 = Ponto(873, 23)


print(p1)
