

class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, other):
        if other[0] < self.centre[0]+self.radius and other[1] < self.centre[1]+self.radius:
            return True
        
        else:
            return False
