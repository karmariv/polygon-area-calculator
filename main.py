# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
#from unittest import main

rectangle = shape_calculator.Rectangle()

rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

print('-----------------------------')
sq = shape_calculator.Square(2)
aa = shape_calculator.Rectangle(width=3,height=6)
print(aa)


# Run unit tests automatically
#main(module='test_module', exit=False)