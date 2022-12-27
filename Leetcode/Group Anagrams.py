from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for item in s:
            if item not in ds:
                ds[item] = 1
            else:
                ds[item] += 1
        for item in t:
            if item not in dt:
                dt[item] = 1
            else:
                dt[item] += 1
        if set(ds.keys()) != set(dt.keys()):
            return False
        else:
            for key in list(ds.keys()):
                if ds[key] != dt[key]:
                    return False
        return True

    def groupAnagrams(self, strs):
        result = []
        string_len = len(strs)
        d = {}
        for index, each in enumerate(strs):
            temp = ""+each[-1]
            if temp not in d.keys():
                d[temp]=[index]#.append(index)
            else:
                d[temp].append(index)
        for k, v in d.items():
            result.append([strs[index] for index in v])
        return result
        

def fun(arr):
    sol = Solution()
    return sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])


if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        print('res -> ',fun(input().split(',')))
        tcs-=1