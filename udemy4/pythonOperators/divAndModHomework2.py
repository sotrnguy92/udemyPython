#write a program that reads 2 numbers and divides them but only prints the decimal part
#input: 201 25
# output: 0.04
# note that 201/25 = 8.04 but we only want the 0.04

num1, num2 = map(float, input("enter 2 numbers:").split())

print("decimal portion of first number divided by second number: ",num1%num2/num2)