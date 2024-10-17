...
10) Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
...
input_line = input()
numbers = tuple(int(num) for num in input_line.split())
x = int(input())

count = numbers.count(x)

factorial = 1
for i in range(1, count + 1):
    factorial *= i

print(factorial)
