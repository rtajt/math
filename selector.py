import add as add
import dieroll as dieroll
import divide as divide
import factorial as factorial
import kinetic as kinetic
import multiply as multiply
import potential as potential
import spring as spring
import subtract as subtract

operation = int(input("Type the number of the operation you want to perform \n0: Addition \n1: Division \n2: Factorials \n3: Kinetic Energy \n4: Multiplication \n5: Potential Energy \n6: Roll A Die \n7: Spring Energy \n8: Subtraction\n"))

match operation:
    case 0:
        add.main()
    case 1:
        divide.main()
    case 2:
        factorial.main()
    case 3:
        kinetic.main()
    case 4:
        multiply.main()
    case 5:
        potential.main()
    case 6:
        dieroll.main()
    case 7:
        spring.main()
    case 8:
        subtract.main()
    case _:
        print("Invalid number")
