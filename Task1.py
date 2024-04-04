import math
import unittest

def circle(radius):
    return math.pi * radius**2
def triangle(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area
def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    max_side = max(sides)
    sides.remove(max_side)
    return max_side**2 == sides[0]**2 + sides[1]**2

class TestGeometry(unittest.TestCase):
    def test_circle(self):
        self.assertAlmostEqual(circle(7), 153.938, places=3)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle(5, 5, 6), 12)

    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertFalse(is_right_triangle(4, 6, 7))

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)