class Solution:
    def swap(self,arr,i,j,k):
        temp = arr[i]+[]
        arr[i] = arr[j]+[]
        arr[j] = temp


    def partition (self,arr, low, high,k):
        # pivot (Element to be placed at right position)
        pivot = arr[high][k]
        i = low-1 #// Index of smaller element and indicates the 
        #  right position of pivot found so far
        for j in range(low,high):
            # // If current element is smaller than the pivot
            if arr[j][k] < pivot:
                i+=1
                self.swap(arr,i,j,k)
        self.swap(arr,i,j,k)
        return (i + 1)

    def sortTheStudents(self, score,k):#List[List[int]], k: int) -> List[List[int]]:
        # To sort the list in place...
         return self.quick_sort(score,0,len(score)-1,k)


    def quick_sort(self,array, low, high,k):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(array, low, high,k)
            # Recursive call on the left of pivot
            self.quick_sort(array, low, pi - 1,k)
            # Recursive call on the right of pivot
            self.quick_sort(array, pi + 1, high,k)
        return array
 
# Driver code
# array = [10, 7, 8, 9, 1, 5]
# quick_sort(array, 0, len(array) - 1)

def fun():
    sol= Solution()
    return sol.sortTheStudents(score=[[10,6,9,1],[7,5,11,2],[4,8,3,15]],k=2)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun())#input().split(',')))
        tcs-=1

