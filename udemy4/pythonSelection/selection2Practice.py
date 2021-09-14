# create a function that prints the last digit of a number if even
# if odd then
#   if <1000 print the last 2 digits
#   if >1000 and <1000000 print the last 4 digits
#   otherwise print the negative of the number
import math


def evenOddPrint():
    num1 = int(input("Enter a number: "));

    if num1%2 == 0:
        print(num1%10);
    elif(num1 < 1000):
        print(num1%100);
    elif num1 > 1000000:
        print(-num1);
    else:
        print(num1%10000);


def last3Digits():
    numLast3 = int(input("Enter a number: "));

    if numLast3 < 10000:
        print("this is a small number.");
    else:
        firstDigit = numLast3%10
        secondDigit = int(numLast3%100/10);
        thirdDigit = int(numLast3%1000/100);

        if (firstDigit+secondDigit+thirdDigit)%2 ==1:
            print("this is a great number.");
        else:
            if firstDigit%2 == 1 or secondDigit%2 == 1 or thirdDigit%2 ==1:
                print("this is a good number");
            else:
                print("this is a bad number");

last3Digits();