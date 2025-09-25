import math  # import math module for using π (pi)


# Function to calculate Surface Area of a Sphere
# Formula: A = 4 * π * r²
def sphereArea(r):
    return 4 * math.pi * r**2


# Function to calculate Volume of a Sphere
# Formula: V = (4/3) * π * r³
def sphereVolume(r):
    return (4 / 3) * math.pi * r**3


# Function to return both surface area and volume of a sphere
def sphereMetrics(r):
    return sphereArea(r), sphereVolume(r)


# Function to calculate Area of a Circle
# Formula: A = π * r²
def circleArea(r):
    return math.pi * r**2


# Function to calculate Area of a Square
# Formula: A = side²
def squareArea(x):
    return x**2
