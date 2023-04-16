def bubble_sort(arr):
    n = len(arr)
    cont = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cont = cont + 1
              
    return cont

#Main------- 
T = int(input())
for i in range(T):
    n = input()
    array = list(map(int,input().split()))
    print(bubble_sort(array))
