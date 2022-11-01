#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 90), Rectangle(150, 60, 0, 150)]
    list_squares = [Square(100, 100, 100)]

    Base.draw(list_rectangles, list_squares)

