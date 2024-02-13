#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		result = self.find_subs( s, 0, len(s), "")
		return sorted(result)
            
    def find_subs(self, inputst, ind, n, res):
        if ind>=n:
            # print('res -> ', res)
            return [res] if res!="" else []
        # consider current
        res1, res2 = [],[]
        # if len(res)>0 and res[-1]>inputst[ind]:
        #     pass
        # else:
        res1 = self.find_subs(inputst, ind+1, n, res+inputst[ind])
        # skip current
        res2 = self.find_subs(inputst, ind+1, n, res+"")
        # print('reult -> ', res1+res2)
        return res1+res2
        
            
            
