class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        cnt1, cnt2 = 0, 0
        el1, el2 = -999, -999 
        for index in range(len(nums)):
            if cnt1==0 and nums[index]!=el2:
                el1 = nums[index]
                cnt1=1
            elif cnt2==0 and nums[index]!=el1:
                el2 = nums[index]
                cnt2=1
            elif nums[index]==el1:
                cnt1+=1
            elif nums[index]==el2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        c1, c2 = 0,0
        for each in nums:
            if each==el1:
                c1+=1
            elif each==el2:
                c2+=1
        res = []
        if c1> int(len(nums)/3):
            res.append(el1)
        if c2>int(len(nums)/3):
            res.append(el2)
        return res


def fun():
    args = [3,2,3]
    sol= Solution()
    return sol.check_freq(args)


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun())
        tcs-=1