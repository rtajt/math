import math
def main():
    num = int(input("What do you want to take the factorial of?"))
    def factorial(x):
        return math.factorial(x)
    print(factorial(num))