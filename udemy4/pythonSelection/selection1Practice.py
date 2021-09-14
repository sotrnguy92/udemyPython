

# #read an integer and print if it has 1, 2, 3, 4, or 5+ digits
def intLength():
    number = input("enter a number: ");

    if len(number) < 5:
        print(len(number));
    else:
        print("5+");




#Create a calculator

def calculator():
    num1, operation, num2 = input("enter what you would like to calculate and include spaces: ").split();

    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
        print(num1, " + ",num2, " = ", num1+num2 );
    elif operation == "-":
        print(num1, " - ",num2, " = ", num1-num2 );
    elif operation == "*":
        print(num1, " * ", num2, " = ", num1 * num2);
    else:
        if num2 == 0:
            print('undefined');
        else:
            print(num1, " / ", num2, " = ", num1 / num2);




# create a function that reads