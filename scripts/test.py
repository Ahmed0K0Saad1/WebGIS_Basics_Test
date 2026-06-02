class property:
    def __init__(self, name:str, price:float, latitude:float, longitude:float):
        self.name = name
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    def calulate_distance(self, area:float):
        return self.price / area
    
p1 = property("House 1", 100000, 40.7128, -74.0060)
d = p1.calulate_distance(0)