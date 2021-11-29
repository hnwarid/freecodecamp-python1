class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.height * self.width
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * self.height + 2 * self.width
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width**2 + self.height **2)**0.5
        return self.diagonal

    def get_picture(self):
        if self.width > 50 or self.height >50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        self.amount_inside = (self.width * self.height) // (shape.width * shape.height)
        return self.amount_inside

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
        self.amount_inside = (self.width ** 2) // (shape.width ** 2)
        return self.amount_inside

    def __str__(self):
        return "Square(side={})".format(self.width)