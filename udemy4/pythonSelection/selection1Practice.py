

#read an integer and print if it has 1, 2, 3, 4, or 5+ digits

number = input("enter a number: ");


if len(number) < 5:
    print(len(number));
else:
    print("5+")