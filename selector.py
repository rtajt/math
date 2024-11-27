import add as add
import dieroll as dieroll
import divide as divide
import factorial as factorial
import kinetic as kinetic
import multiply as multiply
import subtract as subtract

operation = int(input("Type the number of the operation you want to perform \n0: Addition \n1: Division \n2: Factorials \n3: Kinetic Energy \n4: Multiplication \n5: Roll A Die \n6: Subtraction"))

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
        dieroll.main()
    case 6:
        subtract.main()
    case _:
        print("Invalid number")
