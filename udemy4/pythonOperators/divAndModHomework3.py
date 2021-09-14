#write an program that finds the remainder of 2 numbers without using the modulus operator %

num1, num2 = map(float, input("enter 2 numbers: ").split());

print("the remainder of", num1, "/", num2, "is: ", (num1/num2 - int(num1/num2))*num2);