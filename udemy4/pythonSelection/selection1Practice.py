

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




# create a function that reads 2 integers and prints the minimum of the two

def minimum():
    num1, num2 = map(int, input("enter two numbers: ").split());

    if num1 < num2:
        print("the minimum is: ", num1);
    else:
        print("the minimum is: ", num2);


# Create a function that gets the minimum of 3 numbers

def minimum3():
    smallest = 0
    num1, num2, num3 = map(float, input("Enter 3 numbers: ").split())

    if (num1 < num2):
        smallest = num1;
    else:
        smallest = num2;

    if (num3 < smallest):
        smallest = num3;

    print("the smallest number is: ", smallest);

minimum3();
