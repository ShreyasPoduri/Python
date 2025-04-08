class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1416  # Approximate value of pi

    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.pi * self.radius

# user input
radius_input = input("Enter the radius of the circle: ")

radius = float(radius_input)

circle = Circle(radius)

# Calculate and print results
print("Area of the circle:", round(circle.area(), 2))
print("Perimeter of the circle:", round(circle.perimeter(), 2))
