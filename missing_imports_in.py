import os
import sys
import math
import json  
from datetime import datetime 

def calculate_square(numbers):
    return [x ** 2 for x in numbers]

def main():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = calculate_square(numbers)
    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)

if __name__ == "__main__":
    main()
