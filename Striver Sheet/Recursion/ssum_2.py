class Solution:
	def subsetSums(self, arr, N):
		self.res = set()
		self.arr = arr
		self.recur(arr, 0, N)
		return list(self.res)

	def recur(self, psum,ind, N):
		if ind>=N:
			return self.res.add(psum) 
		self.recur(psum, ind+1, N)
		self.recur(psum+self.arr, ind+1, N)

sol = Solution()
arr = []

print(sol.subsetSums(arr, len(arr)))