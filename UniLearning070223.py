def hello():
    print("Hi there")

hello()  # output Hi there

def hello3(name = "whoever"):
    print("hello,", name)

name = "Mirka"
hello3(name)

# basic functions

def divide_by_two(num):
    print (num / 2)

divide_by_two(42)
divide_by_two(12)

# two numbers

def divide_by_nums(num1, num2):
    print(num1/num2)

divide_by_nums(6, 4)
# we can also specify the order
divide_by_nums(num2 = 2, num1 = 10)

# get total

def get_total(items):
    total = 0
    for item in items:
        total = total + item
    return total

items = [3, 5, 7]
t = get_total(items)
print(t)

# function for average

def get_average(tests):
    total = 0
    for test in tests:
        total = total + test
    return total / len(tests)

def print_report(last, first, tests):
    print("Report for {last}, {first}".format(last=last, first=first))
    num = 1
    for test in tests:
        print("Test {num: {grade}".format(num=num, grade=test))
        num = num + 1
    print("*" * 20 )
print("Average: {average}" .format(average=get_average(tests)))

def get_student():
    last = input("Student's last name: ")
    first = input("Student's first name: ")
    return last, first

def get_tests():
    tests =[]
    test = 0

    while True:
        test = input("Test grade: ")
        if test < 0:
            break
        tests.append(test)
    return tests

def main():
    print("This is the grade calculator.")
    last, first = get_student()
    tests = get_tests()
    print_report(last, first, tests)

if __name__ == "__main__":
    main()
