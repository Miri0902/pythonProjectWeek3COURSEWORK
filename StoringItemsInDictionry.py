# create  a dictionary

games = {'checkers': 'board', 'poker': 'card'}
print(games.keys())


# add a value and key
games['cludo'] = 'board'
print(games)

# compare dictionary

d1 = {1: 'one', 2: 'two', 3: 'three'}
d2 = {1: 'one', 2: 'two', 3: 'three'}
d3 = {1: 'one', 3: 'three', 2: 'three'}

d1==d2 # in console

#DELETE an item

d1.pop(1)
print(d1)

# WORKING EXAMPLE = MIGHT BE USEFUL FOR PROJECT

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
print("Average: {average}".format(average=get_average(tests)))

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

    students = {}
    cont = 'y'
    while cont[0].lower() == 'y':

      last, first = get_student()
      name = last + ':' + first

    tests = get_tests()
    students(name) == tests
    cont = input("Another student? ")

for student in students:
    print ("*" * 20)
    last, first = student.split(':')
    print_report(last, first, students[student])

if __name__ == "__main__":
    main()
