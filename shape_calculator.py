import math

class Rectangle:
    width = 0
    height = 0

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def set_width(self,  width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self, width = 0, height = 0):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self, width = 0, height = 0):
       return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        i = 0
        shape = ''

        if (self.width <= 50 and self.height <= 50):
            while i < self.height:
                j = 0

                #Start new line
                while j < self.width:
                    shape = shape + '*'
                    j = j + 1
                
                #Add end of line and jump to next line
                shape = shape + '\n'
                i = i + 1

            return shape         
        else:
            return 'Too big for picture.'
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + (")")
    
    def get_amount_inside(self, shape):
        comp_width = shape.width
        comp_height = shape.height
        
        if comp_width <= self.width and comp_height <= self.height:
            width_fit = math.floor(self.width / comp_width)
            height_fit = math.floor(self.height / comp_height)
           
            return width_fit * height_fit
        else:
            return 0

        
        

class Square(Rectangle):
    width = 0
    height = 0

    def __init__(self, size = 0):
        self.width = size
        self.height = size
    
    def __str__(self):
        return "Square(side=" + str(self.width) + (")")

    def set_side(self, size):
        self.width = size
        self.height = size

    def set_width(self, size):
        self.width = size
        self.height = size

    def set_height(self, size):
        self.width = size
        self.height = size

