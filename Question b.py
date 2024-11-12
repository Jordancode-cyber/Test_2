#This program prints the multiplication table of a given number up to 12

def multiplication_table():
    number = 12
    for i in range(1, 13):
        
            print(f"{number} x {i} = {number * i}")