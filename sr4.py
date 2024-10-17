...
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
...
ans:
n = int(input())
tuple_elements = tuple(int(input()) for _ in range(n))
print(sum(tuple_elements))
