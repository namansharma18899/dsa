class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        index = 0
        max=0
        while(index < len(nums)):
            if nums[index]!=0:
                max-=1
                if nums[index]>max:
                    max = nums[index]
                index+=1
            else:
                #count lens of zeroes
                count = 0
                zdex = 0+index
                for zdex in range((0+index), len(nums)):
                    if nums[zdex]==0:
                        count+=1
                    else:
                        break
                if max<=count:
                    if max==count:
                        if index+count>=len(nums):
                            return True
                    return False
                elif max>count:
                    max-=count
                    index+=count
            print('max -> ', max,index)
        return True
                