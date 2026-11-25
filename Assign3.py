#1.Find the data type of every value in a mixed list.
'''
my_list = [10, 10.5, "Hello", True, [1, 2, 3]]

for i in my_list:
    print(i, ":", type(i))
'''

#2.Convert a nested list into a tuple of tuples.
'''
my_list = [[1, 2], [3, 4], [5, 6]]
result = tuple(tuple(i) for i in my_list)
print(result)
'''

#3.Remove all duplicate values from a mixed list while preserving the original order.
'''
my_list = [10, "hello", 20, 10, "hello", 30, True]
result = []
for i in my_list:
    if i not in result:
        result.append(i)

print(result)
'''

#4.Check whether a number is a power of 2 using operators.
'''
num = 16

if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")
'''

#5.Swap two numbers using bitwise XOR.

a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)