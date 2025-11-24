class Rectangle:
    """
    A class used to represent a Rectangle.Attributes----------
      length : float The length of the rectangle.
    width : float The width of the rectangle.
    """
    def __init__(self, length, width):
        """
        Constructs all the necessary attributes for the rectangle object.
        Parameters length : float
            The length of the rectangle.
        width : float
            The width of the rectangle.
        """
        self.length = length  # store the length of the rectangle
        self.width = width    # store the width of the rectangle
    def area(self):
        """Computes the area of the rectangle.
        Returns
        float The calculated area.
        """
        return self.length * self.width  # area = length × width
    def perimeter(self):
        """Computes the perimeter of the rectangle.
        Returns
        float
            The calculated perimeter.
        """
        return 2 * (self.length + self.width)  # formula for perimeter
r = Rectangle(10, 5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
