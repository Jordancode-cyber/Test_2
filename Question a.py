#This program takes in a list of integers and returns even numbers

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
#To store even numbers
even = []
# To return even numbers
for numbers in list:
    if numbers %2 ==0:
        even.append(numbers)
        
#printing the even numbers
print(f"Even numbers are: {even}")