arr = input().split(',')
arr = [int(x) for x in arr]
time = int(input())
if time==0:
    print([index for index in range(len(arr))])
    exit()
dp_prefix = [1 for each in arr]
dp_suffix = [1 for each in arr]
#precomputing the chain of non increasing for each index
# print(arr)
for index in range(1, len(arr)):
    if arr[index - 1]>= arr[index]:
        dp_prefix[index] = dp_prefix[index - 1] +1
for index in range(len(arr)-2, -1, -1):
    if arr[index + 1]>=arr[index]:
        dp_suffix[index] = dp_suffix[index + 1] +1
res = []
print(dp_prefix, '\n', dp_suffix)
for index in range(time, len(arr)-1-time):
    if dp_prefix[index]>=time+1  and dp_suffix[index]>=time+1:
        res.append(index)
print(res)
# return res