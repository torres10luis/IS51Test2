""" 
We will write a program that will display the number of grades 
using the formula open() method to retrieve it from the final.txt file 
it will also tell us about the average of the grades using the kickstart function
then it will show the percentage of grades that are above the average grade from the total grades
then we will use calculate percent above average function to make calculations
we will then assign grades to a list of intergers to be able to get the number of grades with an average grade and also the percentage
"""

""" 
def main()
    listfinal = []
    list1 = open("final.txt" , "r")
    print(f.read())

    list1 = open("final.txt" , "r")
    counts = 0

    lists = list1.read()
    samelist = lists.split("\n")

    for i in samelist:
        if i: 
            counts += 1

    print("this the number of numbers in list")
    print(counts)

calculate_average()


#print(list1.read())
main()
"""

#working out the details in my psuedo code trying out the ways to make it work
""" import math

list1 = open("final.txt" , "r")
counts = 0

lists = list1.read()
samelist = lists.split("\n")

for i in samelist:
    if i: 
        counts += 1
list1.close()
print(counts / len(lists)) """
""" def calculate_average():
    list1 = open("final.txt" , "r")
    lists = list1.read() 

    with open("final.txt") as l:
        data = [int(line) for line in l]

print('the min is ', min(data))    """
    

""" return sum(lists) / len(lists)

avera = averlist(lists)

print("this the number of numbers in list")
print(counts) 
print("this the number of numbers in list")
print(counts) """