import random
def main():
    die = int(input("What die do you want to roll?"))
    def roll(d):
        return random.randint(1,d)
    print(roll(die))