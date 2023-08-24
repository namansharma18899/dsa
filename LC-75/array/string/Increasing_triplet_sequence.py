class Solution:
    def increasingTriplet(self, num):
        """
        brute force: 
        O(N3)
        """
        for index in range(0, len(num)):
            for j in range(index+1, len(num)):
                if num[j] > num[index]:
                    for k in range(j+1, len(num)):
                        if num[k] > num[j]:
                            return True
        return False




sol = Solution()
arr = []

print(sol.increasingTriplet(arr))