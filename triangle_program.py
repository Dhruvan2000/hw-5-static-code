"""
Name: Dhruvan Dronavalli
Cwid:20016452
Subject: SSW 567
HW 05 - Static Code Analysis
"""
def classify_triangle(side_a, side_b, side_c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """
    # verify that all 3 inputs are positive integers
    if not all(isinstance(side, int) and side > 0 for side in [side_a, side_b, side_c]):
        return 'InvalidInput'

    # Check for Triangle Property: The sum of the length of the two sides
    # of a triangle is greater than the length of the third side.
    if any(side >= (sum(other_sides) - side) for side, other_sides in [
        (side_a, (side_b, side_c)),
        (side_b, (side_a, side_c)),
        (side_c, (side_a, side_b))
    ]):
        return 'NotATriangle'

    # After all checks above, we can classify the triangles
    if side_a == side_b == side_c:
        return 'Equilateral'
    if any(side_a == side_b, side_b == side_c, side_a == side_c):
        return 'Isosceles'
    if any(side_a * 2 + side_b * 2 == side_c ** 2,
           side_a * 2 + side_c * 2 == side_b ** 2,
           side_b * 2 + side_c * 2 == side_a ** 2):
        return 'Right'
    return 'Scalene'

# Example usage:
# print(classify_triangle(3, 4, 5))
