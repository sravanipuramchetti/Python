# If else conditions
a = 10
b = 5
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

print("If else condition is ended")

# Loops in python
obj = (1, 2, 3, 4, 6)
for i in obj:
    print(i)  # This will print the values of obj
    print(i*2)  # this will print the multiples of 2
print("This is end of the Loop block")

# range keyword usage in Loops in python
summation = 0
for j in range(1, 6):  # range means it will take the numbers from 1 to 6-1
    summation = summation +j
print(summation)

# by using range keyword we can change the index
for L in range(1, 10, 2):  # 2 is the index value where the values in range will skip the numbers of 2 index
    print(L)  # 0utput is 1,3,5,7,9

# If the range is in single number then 0 will be considered as 1st index
print("****Default index value when only one range is given***")
for h in range(20):
    print(h)

# While loop in python. the main difference btw loop and while is in while the iteration continue untill condition is satisfied.
print("***While Loop execution *****")
up = 10
while up > 1:
    if up == 9:
        continue
    if up == 5:
        break
    print(up)  # this will print infinite loop if there is no condition below
    up = up - 1  # this is decrease the up value and makes to 1 at end

