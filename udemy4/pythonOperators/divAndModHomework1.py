###
# write a program that reads 5 numbers and prints the following
# A) their average
# B) The sum of the first 3 divided by sum of the last 2
# C) The average of the first 3 divided by the average of the last 2
# What is the mathematical relationship between parts B and C?
###

#getting input from user and splitting it into a list of floats
nums = list(map(float,input("enter 5 numbers: ").split()));

#printing the average of numbers in list nums
print("average of all numbers: ",sum(nums) / len(nums))

#printing sum of first 3 nums divided by sum of last 2
print("sum of first 3/sum of last 2: ",sum(nums[0:3])/sum(nums[3:5]))

#printing average of first 3 nums divided by average of last 2 nums
print("average of first 3/average of last 2: ", (sum(nums[0:3])/3) / (sum(nums[3:5])/2))

#Can also use this print
print("sum of first 3/sum of last 2: ",(sum(nums[0:3])/sum(nums[3:5])) * 2/3)
