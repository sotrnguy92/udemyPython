# Read an integer X then read 6 integers s1, e1, s2, e2, s3, e3
# ○ These 6 numbers are for 3 interval
# ○ Each Interval is a range [start, end]
# ○ Number X in a range if start <= X <= end
# ○ E.g 7 in range [5, 12] but not in range [10, 20]
# ● Print how many intervals that
# X is part of
# ● Inputs
# ○ 7 1 10 5 6 4 40 ⇒ 2
# ■ Number 7 exists in 2 intervals [1, 10] and [4, 40]
# ○ 10 5 15 6 100 3 30 ⇒ 3
# ■ 10 exists in the 3 intervals [5 15], [6 100], [3 30]
# ○ 10 100 200 100 101 120 170 ⇒ 0 [doesn’t exist in any interval

def isInIntervals():
    testNum = int(input("enter a number to test: "));
    intervals = list(map(int, input("enter 6 numbers to use as intervals: ").split()));
    numberOfIncludedIntervals = 0;
    intervalStr = ""


    for i in range(0,6,2):
        if intervals[i]< testNum < intervals[i+1]:
            intervalStr += str(intervals[i:i+2]);
            numberOfIncludedIntervals +=1;

    print(testNum, "exists in the ", numberOfIncludedIntervals, "intervals ", intervalStr);


# Read 4 integers representing 2 intervals and print their intersection interval. If
# they don’t intersect, print -1
# ● Inputs
# ○ 1 6 3 8 ⇒ 3 6
# ■ Interval [1 6] and [3 8] only intersects at [3, 6]
# ■ Why: interval [1, 6] has numbers: {1, 2, 3, 4, 5, 6}
# ■ And: interval [3, 8] has numbers: {3, 4, 5, 6, 7, 8}
# ■ So the intersection is {3, 4, 5, 6} = [3, 6]
# ○ 1 15 20 30 ⇒ -1

def overlappingInterval():
    intervals = list(map(int, input("enter 4 numbers to use as your intervals: ").split()));

    if intervals[0] < intervals[3] and intervals[1] > intervals[2]:
        print("the overlapping interval is: ", [max(intervals[0], intervals[2]), min(intervals[1], intervals[3]) ])

overlappingInterval()