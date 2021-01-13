"""
Troy Hunt
Python Practice
6/1/2018

Light bulb Problem
    This program is used to visually simulate how a row of n number of light bulbs will change after the following
    algorithm occurs:
        - There are an n number of light bulbs in a row. All of them are off.
        - First pass (starting with the first bulb, pulls every switch) (Now every bulb is On)
        - Second pass (starting with the second bulb, pulls every second switch)
        - Third pass (starting with the third bulb, pulls every third switch)
        - This pattern continues until the number of passes would exceed the number of bulbs
        - What is the status of the bulbs at any given pass?
        - 1 is On
        - 0 is Off

"""

#Ask user input. (+1 to display the process starting at 1 and not 0)
tech_numb = int(input("How many light bulbs are in a hall?"))
tech_numb +=1

light_bulbs = []
for i in range(0,tech_numb):
    light_bulbs.append(0)

print(len(light_bulbs)-1)

j = 1
x = 1

while j < len(light_bulbs):

#Iterates through list and +1 if i is a factor of jl

    for i in range(j, len(light_bulbs)):
        if i%j == 0:
            light_bulbs[i] += 1

#Even number of factors = 0 - OFF
#Odd number of factors = 1 - ON

            if light_bulbs[i]%2 == 0:
                light_bulbs[i] = 0

        i == j
    j +=1
    print ("Pass #",x," = ", light_bulbs[1:])
    x +=1

print(input("Press any key to continue..."))
