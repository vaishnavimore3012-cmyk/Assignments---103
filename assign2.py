
#1. Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

'''
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))

result = is_even(num)

print(result)
'''

#2.Write a function largest(a, b) that returns the larger number.
'''
def largest(a, b):
    if a > b:
        return a
    else:
        return b


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = largest(num1, num2)

print("Largest number is:", result)
'''

#3.Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
'''
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)


num = int(input("Enter a number: "))

print_numbers(num)
'''

#4.Write a function sum_n(n) that returns the sum of numbers from 1 to n.
'''
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


num = int(input("Enter a number: "))

result = sum_n(num)

print("Sum of numbers:", result)
'''

#5.Write a function table(n) that prints the multiplication table of n from 1 to 10.
'''
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


num = int(input("Enter a number: "))

table(num)
'''

#6.Write a function that takes a list and returns how many even numbers it contains.
'''
def count_even(numbers):
    count = 0

    for i in numbers:
        if i % 2 == 0:
            count = count + 1

    return count


result = count_even([1, 2, 3, 4, 6])

print(result)
'''

#7. Without using max(), write a function that returns the largest number in a list.
'''
def largest(numbers):
    biggest = numbers[0]

    for i in numbers:
        if i > biggest:
            biggest = i

    return biggest


result = largest([10, 25, 5, 40, 15])

print("Largest number is:", result)
'''

#8. FizzBuzz
#Write a function that prints numbers from 1 to 100.
#If divisible by 3, print "Fizz".
#If divisible by 5, print "Buzz".
#If divisible by both, print "FizzBuzz".

'''
def fizzbuzz():
    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)


fizzbuzz()
'''

# 9.Write a function that returns True if a string is a palindrome.
'''
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


word = input("Enter a string: ")

print(is_palindrome(word))
'''

#10.Write a function that counts the vowels in a string.
'''
def count_vowels(string):
    count = 0

    for char in string:
        if char in "aeiouAEIOU":
            count += 1

    return count


word = input("Enter a string: ")

print("Number of vowels:", count_vowels(word))
'''

#11.Write a function that returns the second largest number in a list without using sort().
'''
def second_largest(numbers):
    largest = numbers[0]
    second = None

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num != largest:
            if second is None or num > second:
                second = num

    return second


numbers = [10, 25, 5, 40, 30]

print("Second largest number:", second_largest(numbers))
'''

#12.Generate a random number between 1 and 10.
#Keep asking the user to guess until they get it right.
#Use a loop, conditionals, and functions.
'''
import random

def guessing_game():
    secret_number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == secret_number:
            print("Congratulations! You guessed it right.")
            break

        elif guess < secret_number:
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")


guessing_game()
'''

# 13. Write a function grade(marks) that:
#Returns "A" for marks ≥ 90
#Returns "B" for marks ≥ 80
#Returns "C" for marks ≥ 70
#Returns "D" for marks ≥ 60
#Otherwise returns "F"

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


marks = int(input("Enter your marks: "))

print("Your grade is:", grade(marks))