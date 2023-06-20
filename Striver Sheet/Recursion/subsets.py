# User function Template for python3
class Solution:
    def recur_sum(self, arr, N, curr_index, sum):
        if curr_index >= N:
            return [sum]
        return self.recur_sum(arr, N, curr_index + 1, sum) + self.recur_sum(
            arr, N, curr_index + 1, sum + arr[curr_index]
        )

    def subsetSums(self, arr, N):
        res = self.recur_sum(arr, N, 0, 0)
        res = sorted(res)
        return res


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")


""""
NOTE: 
time complexity -> Geometric Progresssion...  
space complxtiy -> Stack occupy TODO: COULDN'T FIND OUT 

"""