my_file = open ("datafile.txt", "r")

for line in my_file.readlines():
    print(line)

my_file.close()

# the previous code can be rewritten to test for exceptions

try:
    my_file = open("datafile.txt", "r")

    for line in my_file.readlines():
        print(line)
finally:
    my_file.close()