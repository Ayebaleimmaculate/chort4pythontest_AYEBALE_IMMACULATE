# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.

def sum_numbers():
    total = 0
    while True:
        num = float(input("Enter a number (or 0 to stop): "))
        if num == 0:
            break
        total += num
    
    print(f"Total sum of the number entered is : {total}")

sum_numbers()




# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
def print_odd_numbers():
    for num in range(1, 101):
        if num % 2 != 0:
            print(num)

print_odd_numbers()

