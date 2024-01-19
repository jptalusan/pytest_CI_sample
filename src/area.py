def calculate_area_square(length: int | float) -> int | float:
    """
    Function to calculate the area of a square
    :param length: length of the square
    :return: area of the square
    """
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length


def calculate_area_triangle(base: int | float, height: int | float) -> int | float:
    """
    Function to calculate the area of a triangle
    :param base: base of the triangle
    :param height: height of the triangle
    :return: area of the triangle
    """
    if not isinstance(height, (int, float)) or height <= 0:
        raise TypeError("height must be a positive non-zero number")
    if not isinstance(base, (int, float)) or base <= 0:
        raise TypeError("base must be a positive non-zero number")

    return 0.5 * base * height
