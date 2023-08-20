arr = input().split(',')
arr = [int(x) for x in arr]
p1, p2 = 0, -1

def swap(arr, i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for index in range(0, len(arr)):
    if arr[index]!=0:
        swap(arr, index, p1)
        p1+=1

print(arr)

