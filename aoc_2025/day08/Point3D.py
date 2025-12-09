class Point3D:
    """A 3D point implementation with (x, y, z) coordinates"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dist2(self, p):
        """Calculate the square of the distance between 2 points"""
        return (self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z - p.z) ** 2

    def __str__(self):
        """String representation of the 3D point used by the print() method"""
        return f'Point3D({self.x},{self.y},{self.z})'
