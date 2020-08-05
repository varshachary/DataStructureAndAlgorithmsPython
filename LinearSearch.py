"""Given an array of N elements and a integer K. Your task is to return the position of first occurence of K in the given array.
Note: Position of first element is considered as 1."""
#GeeksforGeeks

for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    flag = -1
    for i in range(n):
        if arr[i] == k:
            flag=i+1
            break
    print(flag)
 
