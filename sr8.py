...
8) Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
...
input_line = input()
numbers = tuple(int(num) for num in input_line.split())
total = 0
for number in numbers:
    total += number
print(total)
