# loops
# counting loop for items in list:

# range (10) gives us list of numbers from 0 - 9
# we can ask for range by using step eg by 2 range(0, 10, 2) will print, 0,2,4,6,8
# we can do it backwards as well range(5, 0, -1) will print 5,4,3,2,1

# using for loop

drinks = ['coffee', 'cola', 'tea']
for drink in drinks:
    print(drink)

# using continue to run the code if it does not find the i
for i in range(1, 7, 2):
    if i == 3:
        print("My favourite!")
        continue
    print("number:", i)

# using break to stop running the code

for i in range(1, 7, 2):
    if i == 3:
        print("My favourite!")
        break # this will exit the loop
    print("number:", i)

# example
cart = [10, 45, 100, 20]
total = 0
for item in cart:
    total = total + item
print(total)

for item in cart:
    if item >= 100:
        print("You need insurance!")
        insurance = True
        break
    insurance = False

# CONDITIONAL LOOP WHILE
# will run while something is true

c = "y"
while c != "n":# by entering n the loop with finish
    c = input("Continue?")

n = 0
while True:
    n = n + 1
    print(n)
    break  # without break it would run indefinitelly

age = ""
age.isdigit()
while not age.isdigit():
    age = input("age: ")
print(age)

# while loop with multiple conditions

items = []
while True:
   item = input("item: ")
   if item == "quit":  # if we enter quit instead of item, it would stop
       break
   items.append(item)
   if len(items) == 5:
       print("that is enough!")
       break

## example extended

print ("This is the grade calculator.")

last = input("Student's last name: ")
first = input("Student's first name: ")

tests = []

while True:
    test = int(input("Test grade: "))
    if test < 0:
        break
    tests.append(test)

total = 0
for test in tests:
    total = total + test

average = total / len(tests)

num = 1
for test in tests:
    print("test {num}: {grade}" .format(num=num,grade=test))
    num = num + 1
print("*" * 20)
print("Average: {average}" .format(average=average))
# to check if the list has the scores, type test in console, or print(test)

print(test)
