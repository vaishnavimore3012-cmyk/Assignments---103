#1. Write a Python program to reverse a number without converting it into a string.
'''
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)
'''

#2. Write a program to check whether a number is a palindrome.
'''
num = int(input("Enter a number: "))
temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if temp == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
'''

#3. Write a program to check whether a number is an Armstrong number.
'''
num = int(input("Enter a number: "))
temp = num
total = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if temp == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
'''

#4. Write a program to find the factorial of a number using a loop.
'''
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)
'''

#5. Write a program to generate the Fibonacci series up to N terms.
'''
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
'''

#6. Write a program to check whether a number is prime.
'''
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
'''

#7. Write a program to print all prime numbers between 1 and 100.
'''
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
'''

#8. Write a program to find the GCD and LCM of two numbers.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
'''

#9. Write a program to reverse a string without using slicing.
'''
text = input("Enter a string: ")
reverse = ""

for i in text:
    reverse = i + reverse

print("Reversed string:", reverse)
'''

#10. Write a program to check whether a string is a palindrome.
'''
text = input("Enter a string: ")
reverse = ""

for i in text:
    reverse = i + reverse

if text == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")
'''

#11. Write a program to count vowels, consonants, digits and special characters in a string.
'''
text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for i in text:
    if i.lower() in "aeiou":
        vowels += 1

    elif i.isalpha():
        consonants += 1

    elif i.isdigit():
        digits += 1

    elif not i.isspace():
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)
'''

#12. Write a program to find the frequency of each character in a string.
'''
text = input("Enter a string: ")

freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Character frequency:")

for i in freq:
    print(i, ":", freq[i])
'''

#13. Write a program to find the first non-repeating character in a string.
'''
text = input("Enter a string: ")

freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in text:
    if freq[i] == 1:
        print("First non-repeating character:", i)
        break
else:
    print("No non-repeating character found")
'''

#14. Write a program to remove duplicate characters from a string.
'''
text = input("Enter a string: ")

result = ""

for i in text:
    if i not in result:
        result = result + i

print("String after removing duplicates:", result)
'''

#15. Write a program to check whether two strings are anagrams.
'''
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")
'''

#16. Write a program to find the longest word in a sentence.
'''
sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)
print("Length:", len(longest))
'''

#17. Find the second-largest element in a list without using sort().
'''
numbers = [10, 20, 5, 40, 30]

largest = numbers[0]
second = None

for i in numbers:
    if i > largest:
        second = largest
        largest = i

    elif i < largest:
        if second == None or i > second:
            second = i

print("Second largest:", second)
'''

#18. Remove duplicate elements from a list without using set().
'''
numbers = [1, 2, 2, 3, 4, 4, 5]

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print("List after removing duplicates:", result)
'''

#19. Find the common elements between two lists.
'''
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for i in list1:
    if i in list2:
        if i not in common:
            common.append(i)

print("Common elements:", common)
'''

#20. Move all zeros to the end of a list without changing the order of other elements.
'''
numbers = [0, 1, 0, 3, 12]

result = []

for i in numbers:
    if i != 0:
        result.append(i)

zeros = numbers.count(0)

for i in range(zeros):
    result.append(0)

print("Updated list:", result)
'''

#21. Find the missing number in a list containing numbers from 1 to N.
'''
numbers = [1, 2, 3, 5, 6]

n = 6

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing number:", missing)
'''

#22. Find the maximum difference between two elements where the larger element appears after the smaller element.
'''
numbers = [2, 7, 1, 8, 3, 10]

max_diff = -1

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        diff = numbers[j] - numbers[i]

        if diff > max_diff:
            max_diff = diff

print("Maximum difference:", max_diff)
'''

#23. Rotate a list to the right by K positions.
'''
numbers = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    last = numbers.pop()
    numbers.insert(0, last)

print("Rotated list:", numbers)
'''

#24. Find all pairs in a list whose sum equals a given target.
'''
numbers = [2, 4, 3, 5, 7, 8, 1]
target = 9

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
'''

#25. Write a program to count the frequency of each word in a paragraph.
'''
paragraph = "Python is easy and Python is powerful"

words = paragraph.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)
'''

#26. Write a program to merge two dictionaries. If a key exists in both, add their values.
'''
dict1 = {
    "apple": 10,
    "banana": 20,
    "orange": 30
}

dict2 = {
    "banana": 15,
    "orange": 25,
    "grapes": 40
}

result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)
'''

#27. Write a program to sort a dictionary based on its values.
'''
marks = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 75,
    "Sneha": 88
}

sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1]))

print(sorted_marks)
'''

#28. Given a list of student dictionaries containing name and marks, find the student with the highest marks.
'''
students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 92},
    {"name": "Amit", "marks": 75},
    {"name": "Sneha", "marks": 88}
]

highest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

print("Topper:", highest["name"])
print("Marks:", highest["marks"])
'''

#29. Group words from a list based on their first character using a dictionary.
'''
words = ["apple", "ant", "banana", "ball", "cat", "car", "dog", "doll"]

grouped = {}

for word in words:
    first_char = word[0]

    if first_char in grouped:
        grouped[first_char].append(word)
    else:
        grouped[first_char] = [word]

print(grouped)
'''

#30. Convert two lists into a dictionary, where the first list contains keys and the second contains values.
'''
keys = ["name", "age", "city", "salary"]

values = ["Vaishnavi", 24, "Pune", 30000]

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)
'''

#31. Write a recursive function to calculate the factorial of a number.
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5

result = factorial(num)

print("Factorial:", result)
'''

#32. Write a recursive function to find the sum of digits of a number.
'''
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

num = 1234

result = sum_digits(num)

print("Sum of digits:", result)
'''

#33. Implement your own map() function without using Python's built-in map().
'''
def my_map(function, numbers):
    result = []

    for num in numbers:
        result.append(function(num))

    return result


def square(n):
    return n * n


numbers = [1, 2, 3, 4, 5]

output = my_map(square, numbers)

print(output)
'''

#34. Implement a function that accepts a list and returns a new list containing only even numbers.
'''
def even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output = even_numbers(numbers)

print(output)
'''

#35. Write a function to flatten a nested list.
'''
def flatten_list(nested_list):
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result

numbers = [1, [2, 3], [4, [5, 6]], 7]

print(flatten_list(numbers))
'''

#36. Student Management System

#Create a console-based application with the following operations:
#- Add student
#- Display all students
#- Search student by ID
#- Update student details


students = []

def add_student():
    student_id = input("Enter Student ID: ")

    # Check whether ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    marks = float(input("Enter Student Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Details ---")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("----------------------")


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            return

    print("Student not found!")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")

            elif choice == "2":
                student["age"] = int(input("Enter new age: "))

            elif choice == "3":
                student["marks"] = float(input("Enter new marks: "))

            else:
                print("Invalid choice!")
                return

            print("Student details updated successfully!")
            return

    print("Student not found!")


# Main Menu
'''
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Update Student Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
'''

#37. Bank Account Management

#Create a bank account program with:
#- Create account
#- Deposit money
#- Withdraw money
#- Check balance
#- Display account details

'''
class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    # Create account
    def create_account(self):
        print("\nAccount created successfully!")

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Rs.", amount, "deposited successfully!")
        else:
            print("Invalid deposit amount!")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Rs.", amount, "withdrawn successfully!")
        else:
            print("Insufficient balance!")

    # Check balance
    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    # Display account details
    def display_details(self):
        print("\n----- Account Details -----")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Account Balance: Rs.", self.balance)


# Main program
print("===== BANK ACCOUNT MANAGEMENT SYSTEM =====")

account = None

while True:
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        if account is not None:
            print("Account already exists!")
        else:
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Deposit: "))

            if balance < 0:
                print("Invalid initial deposit!")
            else:
                account = BankAccount(acc_no, name, balance)
                account.create_account()

    elif choice == '2':
        if account is None:
            print("Please create an account first!")
        else:
            amount = float(input("Enter deposit amount: Rs. "))
            account.deposit(amount)

    elif choice == '3':
        if account is None:
            print("Please create an account first!")
        else:
            amount = float(input("Enter withdrawal amount: Rs. "))
            account.withdraw(amount)

    elif choice == '4':
        if account is None:
            print("Please create an account first!")
        else:
            account.check_balance()

    elif choice == '5':
        if account is None:
            print("Please create an account first!")
        else:
            account.display_details()

    elif choice == '6':
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice! Please try again.")
'''

 #38. Employee Salary Management

#Create a program to:
#- Add employee details
#- Calculate gross salary
#- Calculate deductions
#- Calculate net salary
#- Display employee salary details


# Employee Salary Management System

# Add employee details
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Calculate allowances
hra = basic_salary * 0.20
da = basic_salary * 0.10

# Calculate gross salary
gross_salary = basic_salary + hra + da

# Calculate deductions
pf = basic_salary * 0.12
tax = basic_salary * 0.05

total_deductions = pf + tax

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display employee salary details
print("\n===== EMPLOYEE SALARY DETAILS =====")
print("Employee ID      :", emp_id)
print("Employee Name    :", name)
print("Basic Salary     : Rs.", basic_salary)
print("HRA (20%)        : Rs.", hra)
print("DA (10%)         : Rs.", da)
print("Gross Salary     : Rs.", gross_salary)
print("PF (12%)         : Rs.", pf)
print("Tax (5%)         : Rs.", tax)
print("Total Deductions : Rs.", total_deductions)
print("Net Salary       : Rs.", net_salary)

