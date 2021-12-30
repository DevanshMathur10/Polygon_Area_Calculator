# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(10,9)
print(rect.get_area())
rect.set_width(30)
print(rect.get_perimeter())
print(rect.get_picture())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_width(5)
print(sq.get_diagonal())
print(sq.get_picture())
print(sq)

rect.set_height(10)
rect.set_width(20)
print(rect.get_amount_inside(sq))

# Run unit tests automatically
main(module='test_module', exit=False)