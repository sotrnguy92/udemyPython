# ● Given a starting integer X and an ending integer Y, print all integers between
# X and Y inclusive, each on a line.
# ● Input 3 7
# ● Output
# ○ 3
# ○ 4
# ○ 5
# ○ 6
# ○ 7

def rangePrint():
    x = int(input("enter a starting value: "))
    y = int(input("Enter an ending value: "))
    while x <= y:
        print(x);
        x += 1;

# ● Read integer N and string S.
# ● Print S repeated N times as below
# ● Input: 5 Hi
# ● Output: HiHiHiHiHi
# ● Note: we can use string * 5
# ○ Please use while loops

def repeatString():
    inStr = input("enter a string to repeat: ");
    inNum = int(input("How many times do you want to repeat? "));
    outStr = ""

    while inNum > 0:
        outStr += inStr;
        inNum -=1;

    print(outStr);


# Read integer N.
# ● Print a face down left angled triangle that has N rows as in picture

def createDownTriangle():
    num = int(input("How big do you want the triangle? "));
    while num > 0:
        print ("*" * num);
        num -= 1;



# ● Read integer N, followed by reading N numbers
# ○ Each on separate lines
# ● Print 2 values
# ○ The average of the numbers in odd positions (1st, 3rd, 5th, …)
# ○ The average of the numbers in even positions (2nd, 4th, 6th, …)
# ● Explantation
# ○ (10+20+30)/3 = 20
# ○ (100+200+600)/3 = 300

def specialAverage():
    nums = int(input("How many numbers would you like to enter?: "));
    oddSum = 0;
    evenSum = 0;

    x = 1
    oddCount = 0;
    evenCount = 0;
    while x <= nums:
        enterNum = int(input("Enter a number:"));
        if x%2 == 0:
            evenSum += enterNum;
            evenCount += 1;
        else:
            oddSum += enterNum;
            oddCount += 1;

        x += 1;

    print("average of numbers in the odd position: ", oddSum/oddCount);
    print("average of numbers in the even position: ", evenSum/evenCount);

