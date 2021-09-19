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

