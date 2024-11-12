#This program finds the largest number in a list

list= [1, 2, 3, 4, 5, 6]

large_number = list[5]
#looping the program
for number in list:
    if number > large_number:
        large_number = number
        
#Printing
print(f"The largest number is: {large_number}")
    