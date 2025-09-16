class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def getArea(self):
        area = self.__length * self.__width
        return f"Area = {area}"

    def getPerimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        return f"Perimeter = {perimeter}"

    def isSquare(self):
        if self.__length == self.__width:
            return "This is a square."
        else:
            return "This is not a square."

    def __str__(self):
        return f"Rectangle(length={self.__length}, width={self.__width})"


rect = Rectangle(5,5)
print(rect.getArea())
print(rect.getPerimeter())
print(rect.isSquare())
