class Cylinder:

    def __init__(self,height=1,radius=1):
        self.heigth = height
        self.radius = radius
    
    def volume(self):
        return 3.14*(self.radius)**2*self.heigth
    
    def surface_area(self):
        return (2*3.14*self.radius*self.heigth)+(2*3.14*(self.radius)**2)
    



c = Cylinder(2,3)

c.volume()
print(c.volume())


c.surface_area()
print(c.surface_area())