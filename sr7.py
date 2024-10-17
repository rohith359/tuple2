...
7) Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
...
input_values = input()
tuple_values = tuple(map(int, input_values.split()))
x = int(input())
count_x = tuple_values.count(x)
print(count_x)
