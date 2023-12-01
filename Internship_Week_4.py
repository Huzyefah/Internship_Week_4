import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        print("Hexagon:")
        print("Area:", self.calcArea())
        print("Perimeter:", self.calcPeri())
        print("Sum of Angles:", self.calcAngleSum())
        print()

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length ** 2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print("Square:")
        print("Area:", self.calcAreaSquare())
        print("Perimeter:", self.calcPeriSquare())
        print()

def main():
    cnic = 7
    hexagon_side_length = cnic
    square_side_length = hexagon_side_length + 1

    hexagon = Hexagon(hexagon_side_length)
    square = Square(square_side_length)

    while True:
        print("Menu:")
        print("1. Hexagon")
        print("2. Square")
        print("Any other key to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hexagon.display()
        elif choice == '2':
            square.display()
        else:
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
