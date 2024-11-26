import add as add
import dieroll as dieroll
import divide as divide
import factorial as factorial
import multiply as multiply
import subtract as subtract

operation = int(input("Type the number of the operation you want to perform \n0: Addition \n1: Roll A Die \n2: Division \n3: Factorials \n4: Multiplication \n5: Subtraction"))

match operation:
    case 0:
        add.main()
    case 1:
        dieroll.main()
    case 2:
        divide.main()
    case 3:
        factorial.main()
    case 4:
        multiply.main()
    case 5:
        subtract.main()
    case _:
        print("Invalid number")