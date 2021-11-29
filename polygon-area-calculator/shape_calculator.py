class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width**2 + self.height ** 2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        return (self.width * self.height) // (shape.width * shape.height)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    
class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def set_side(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, width):
        self.set_side(width)

    def get_amount_inside(self, shape):
        return (self.width ** 2) // (shape.width ** 2)

    def __str__(self):
        return "Square(side={})".format(self.width)
