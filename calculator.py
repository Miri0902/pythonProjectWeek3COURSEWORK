#This is a function that performs multiplication using addition only
def multiply(n, m):
    ans = 0
    for i in range(m):
        ans += n
    return ans

#  This is a function that performs division using subtraction only, and returns both quotient and remainder as a tuple

def divide(p, q):
    quotient = 0
# repeat for as long as the first number is bigger than the second one
    # in other words, repeat until p cannot be divided by q anymore.
    # if, in the first iteration, p<q, then the loop won't be executed.
    while p >= q:
        p = p - q
        quotient += 1
    return quotient, p

def add(n,m):
    return n+m

def subtract(n,m):
    return n-m


# Define possible operations as a list
operations = [1,2,3,4]
while (True): # repeat unitl the user wants to stop
    operation = int(input("Select an operation:\n"
                          "(1) Add\n"
                          "(2) Subtract\n"
                          "(3) Multipla\n"
                          "(4) Divide\n"))
#check that this is a valid operation
if operation in operations:
    number1 = float(input("Enter a first number: "))
    number2 = float(input("Enter a second number: "))
else:
    print("This is not a valid operation!")
    continue     # skip this iteration, and start anew!
if operation == 1:
    result = add(number1,number2)
    print(number1,"+",numer2,"=",result)
elif operation == 2:
    result = subtract(number1,number2)
    print(number1, "-", number2, "=", result)
elif operation == 3:
    result = multiply(number1, number2)
    print(number1, "x", number2, "=", result)
elif operation == 4:
    result = divide (number1, number2)
    print(number1, "/", number2, "=""and the remainder is ",result[1])
    continue = input("Do you want to do another operation? (yes/no)"
if continue == "no":
        break

