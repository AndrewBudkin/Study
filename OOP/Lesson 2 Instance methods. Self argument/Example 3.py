class Point():
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, instance):
        if isinstance(instance, Point):
            return ((self.x - instance.x) ** 2 + (self.y - instance.y) ** 2) ** 0.5
        else:
            print("Передана не точка")
