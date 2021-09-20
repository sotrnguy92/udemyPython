# Special Calculator
# ● Design a small application that keeps asking the user 3 choices:
# ○ Enter 1 to sum integers from 1 to N
# ○ Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
# ■ Expect 3 items. Operations are: + - * / // **
# ○ Enter 3 to end the program
# ● The user should input value from 1 to 3
# ○ Otherwise, inform that this is invalid and try again
# ● Take proper input from the user and compute the answer
# ○ See next console simulation

def specialCalculator():

    choice = int(input("Menu: \n"
                       "enter 1 sum the integers from 1 to N\n"
                       "enter 2 to evaluate simple 2 numbers expressions\n"
                       "enter 3 to end the program \n"
                       "\n"
                       "Enter a choice: "))

    while choice != 3:
        if choice > 3:
            print("invalid choice...try again")
        elif choice == 1:
            summation = int(input("enter a number: "))
            total =0
            x = 1
            while x <= summation:
                total += x;
                x += 1;
            print ("the sum from 1 to ", summation, "is ", total );
            choice = int(input("\n Menu: \n"
                           "enter 1 sum the integers from 1 to N\n"
                           "enter 2 to evaluate simple 2 numbers expressions\n"
                           "enter 3 to end the program \n"
                           "\n"
                           "Enter a choice: "))
        elif choice == 2:
            x = eval(input("input something to evaluate: "))
            print(x)
            choice = int(input("\n Menu: \n"
                               "enter 1 sum the integers from 1 to N\n"
                               "enter 2 to evaluate simple 2 numbers expressions\n"
                               "enter 3 to end the program \n"
                               "\n"
                               "Enter a choice: "))



specialCalculator()