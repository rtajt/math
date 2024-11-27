def main():
    springconstant = float(input("What's your spring constant?"))
    deltax = float(input("What's the change in x? (in meters)"))
    def springenergy(k,x):
        solution = 0.5 * k * pow(x,2)
        return solution
    print("The spring energy is " + str(springenergy(springconstant, deltax)) + " Joules")