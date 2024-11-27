def main():
    mass = float(input("What's the mass of your object? (in kilograms)"))
    velocity = float(input("What's the object's velocity? (in meters per seconds)"))
    def kinetic(m,v):
        solution = 0.5 * m * pow(v,2)
        return solution
    print("The kinetic energy is " + str(kinetic(mass, velocity)) + " Joules")