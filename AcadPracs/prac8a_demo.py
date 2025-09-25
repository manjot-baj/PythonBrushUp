# demo.py
import prac8a_geometry as geometry  # importing our custom geometry module


# Function to calculate volume of a pointy 3D shape (like a pyramid or cone)
# Formula for pyramid (square base): V = (1/3) * base_area * height
# Formula for cone (circular base): V = (1/3) * base_area * height
def pointyShapeVolume(x, h, square):
    if square:
        # If shape has a square base → use square area
        # Square area formula: A = side²
        base = geometry.squareArea(x)
    else:
        # If shape has a circular base → use circle area
        # Circle area formula: A = π * r²
        base = geometry.circleArea(x)

    # Apply volume formula: V = (1/3) * base_area * height
    return h * base / 3.0


# List all functions and attributes in the imported module
print(dir(geometry))

# Example: Calculate volume of a square-based pyramid
# Input: side = 4, height = 2.6
# Volume = (1/3) * (side²) * height = (1/3) * (16) * 2.6 = 13.866...
print(pointyShapeVolume(4, 2.6, True))
