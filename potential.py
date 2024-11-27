def main():
    mass = float(input("What's the mass of the object? (in kilograms)"))
    height = float(input("What height is the object at? (in meters)"))
    def potential(m,h):
        solution = m * 9.81 * h
        return solution
    print("The potential energy is " + str(potential(mass, height)) + " Joules")