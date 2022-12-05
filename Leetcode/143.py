from utils.utility import swap
def fun(arr):
    # a b c d e  
    # a e b d c 
    for index in range(1,int(len(arr)/2)):
        if index%2!=0:
            swap(arr, index, index+1)
            swap(arr, index, len(arr)-index)
        print(arr)
    return arr

#    3 swaps 
# 1. a[i], a[i+1]
# 2.    a[n-i], a[i]


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(' ')))
        tcs-=1