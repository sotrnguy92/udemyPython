# ● Read 10 numbers and find which of them has the biggest value and print it.
# ● Inputs (each integer on a seperate line)
# ○ 1
# ○ 67
# ○ -9
# ○ 88
# ○ -45
# ○ 129
# ○ 90
# ○ 65
# ○ 77
# ○ 34
# ● Output ⇒ 129
# ● Restriction: In your whole code there should be 2 variables defined ONLY

def max10():
    biggest = 0;

    for i in range(10):
        num = int(input("enter a number: "));
        if num > biggest:
            biggest = num;

    print(biggest);

# ● Read an integer N (1 <= N <= 10)
# ● Then read N numbers, find which of them has the biggest value and print it.
# ● Inputs (but they will be on seperate lines)
# ○ 5 1 3 2 4.5 2 ⇒ 4.5
# ■ 5 means read 5 integers
# ■ Then we read them [1 3 2 4.5 2]. Their maximum is 4.5
# ○ 10 1 67 -9 88 -45 129 90 65 77 34 ⇒ 129
# ■ Same as last homework. This time we are given first N (10)

def maxUpTo10Values():
    numOFValues = int(input("How many numbers would you like to enter?"));
    biggest = 0;
    print(biggest)
    for i in range(numOFValues):
        num = int(input("enter a number: "));
        if biggest == False or num > biggest:
            biggest = num;

    print(biggest);

maxUpTo10Values()

