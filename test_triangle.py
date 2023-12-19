"""
Name: Dhruvan Dronavalli
Cwid:20016452
Subject: SSW 567
HW 05 - Static Code Analysis
"""
import unittest
from triangle_program import classify_triangle

class TestTriangles(unittest.TestCase):
    'This class contains tests for the classify_triangle function'

    def test_invalid_input_zero_side(self):
        'Test case 1: Invalid input with a zero side'
        self.assertEqual(classify_triangle(3, 4, 0), 'InvalidInput')

    def test_invalid_input_negative_sides(self):
        'Test case 2: Invalid input with negative sides'
        self.assertEqual(classify_triangle(-1, -4, 5), 'InvalidInput')

    def test_valid_input(self):
        'Test case 3: Valid input'
        self.assertNotEqual(classify_triangle(3, 4, 5), 'InvalidInput')

    def test_not_a_triangle_large_side(self):
        'Test case 4: Not a triangle with a large side'
        self.assertEqual(classify_triangle(10, 2, 3), 'NotATriangle')

    def test_not_a_triangle_valid_triangle(self):
        'Test case 5: Not a triangle with valid sides'
        self.assertNotEqual(classify_triangle(3, 4, 5), 'NotATriangle')

    def test_not_a_triangle_valid_isosceles(self):
        'Test case 6: Not a triangle with valid isosceles sides'
        self.assertNotEqual(classify_triangle(5, 5, 8), 'NotATriangle')

    def test_right_triangle_valid_sides(self):
        'Test case 7: Right triangle with valid sides'
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

    def test_right_triangle_invalid_sides(self):
        'Test case 8: Right triangle with invalid sides'
        self.assertNotEqual(classify_triangle(11, 11, 10), 'Right')

    def test_equilateral_triangle_valid_sides(self):
        'Test case 9: Equilateral triangle with valid sides'
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral')

    def test_equilateral_triangle_invalid_sides(self):
        'Test case 10: Equilateral triangle with invalid sides'
        self.assertEqual(classify_triangle(4, 4, 4), 'Equilateral')

    def test_equilateral_triangle_valid_isosceles_sides(self):
        'Test case 11: Equilateral triangle with valid isosceles sides'
        self.assertNotEqual(classify_triangle(4, 8, 10), 'Equilateral')

    def test_isosceles_triangle_valid_sides(self):
        'Test case 12: Isosceles triangle with valid sides'
        self.assertEqual(classify_triangle(4, 4, 5), 'Isosceles')

    def test_isosceles_triangle_valid_isosceles_sides(self):
        'Test case 13: Isosceles triangle with valid isosceles sides'
        self.assertEqual(classify_triangle(5, 5, 8), 'Isosceles')

    def test_isosceles_triangle_invalid_equilateral_sides(self):
        'Test case 14: Isosceles triangle with invalid equilateral sides'
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Isosceles')

    def test_scalene_triangle_valid_sides(self):
        'Test case 15: Scalene triangle with valid sides'
        self.assertEqual(classify_triangle(4, 8, 10), 'Scalene')

    def test_scalene_triangle_valid_sides(self):
        'Test case 16: Scalene triangle with valid sides'
        self.assertEqual(classify_triangle(5, 9, 11), 'Scalene')

    def test_scalene_triangle_invalid_equilateral_sides(self):
        'Test case 17: Scalene triangle with invalid equilateral sides'
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

