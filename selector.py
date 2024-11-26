import add as add
import dieroll as dieroll
import divide as divide
import factorial as factorial
import multiply as multiply
import subtract as subtract

operation = int(input("Type the number of the operation you want to perform \n0: Addition \n1: Division \n2: Factorials \n3: Multiplication \n4: Roll A Die \n5: Subtraction"))

match operation:
    case 0:
        add.main()
    case 1:
        divide.main()
    case 2:
        factorial.main()
    case 3:
        multiply.main()
    case 4:
        dieroll.main()
    case 5:
        subtract.main()
    case _:
        print("Invalid number")
