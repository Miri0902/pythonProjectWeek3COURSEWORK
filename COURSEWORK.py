# loading the file
try:
    my_file = open("epl.txt", "r")

    teams = []

    for line in my_file:
        data = line.split(":")
        teams.append(data)

finally:
    my_file.close()
selection = 0
while selection != 6:
    print("Please select one of the following:")
    print("1. View the table")
    print("2. See/change the top scorer")
    print("3. See/change club manager")
    print("4. Input team results")
    print("5. Declare relegation and promotion with champion results")
    print("6. Quit")
    selection = int(input("Enter your selection (1-6):"))

# we have to create class Table
#import Table *

#for i in selection:
 #    if i = 1:
  #       print(table)
   #  elif i = 2:
    #     print(top scorer)
   #  else:
    #     if i = 6:
     #        print("Quit")



