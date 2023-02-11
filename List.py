nums = [1, 2, 3, 3, 4]
nums[1] = 2.1 # will change 2 to 2.1
len(nums)
nums.count(3) # how many times something occurs
nums.index(2.1) # what index is number 2
2 in nums # will return True is 2 is in the list

# empty list to add to it

children = []
children.append("Jacob")
children.append("Hannah")
print(children)

# extend one list with the content of another one
toppings = ['cheese', 'sause']
additional = ['onions', 'olives']
toppings.extend(additional)
print(toppings)

# to remove an item

toppings.remove('olives')
print(toppings)

# do maths with lists

[1,3] + [4,8] # run in python console
[1,3] * 3

drinks = ['soda', 'tea', 'coffee']
snacks = ['cookies', 'crackers', 'nuts']
drinks.append('hot tea')

print(drinks)

# we now have two tea in the list, to change one to cold tea
# get the index of tea
drinks.index('tea')

# to update

drinks[1] = 'cold tea'
print(drinks)

# we now create a menu

menu = drinks + snacks
print(menu)

# order items in the list
colours = ['red', 'yellow', 'blue']
colours.sort()
print(colours)

# in reverse order
colours.reverse()
print(colours)

# compare lists
a = [1, 3, 4]
b = [1, 3, 4]
a == b # run this in a console

print ("This is the grade calculator.")

last = input("Student's last name: ")
first = input("Student's first name: ")

test = []

test1 = int(input("First test: "))
test.append(test1)
test2 = int(input("Second test: "))
test.append(test2)
test3 = int(input("Third test: "))
test.append(test3)
average = int(test[0] + test[1] + test[2]) / len(test)

report = "{last}, {first}\n\
Test1: {test1}\n\
Test2: {test2}\n\
Test3: {test3}\n\
=============\n\
Average {average}"

print(report.format(last=last, first=first,
                    test1=test1, test2=test2,
                    test3=test3,
                    average=average))

# to check if the list has the scores, type test in console, or print(test)

print(test)
