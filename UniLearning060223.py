print ("This is the grade calculator.")

last = input("Student's last name: ")
first = input("Student's first name: ")

test1 = int(input("First test: "))
test2 = int(input("Second test: "))
test3 = int(input("Third test: "))

average = (test1 + test2 + test3) / 3

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