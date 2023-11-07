class Root:
    def NthRoot(self,  n: int, m: int):
        arr = [ind for ind in range(100)]
        result = []
        
        def root_helper(arr, l, r):
            if l==r:
                return True if n ** arr[l] == m else False
            mp = int()
            l = 0
            r = len(arr)
            lsar = arr[l:mp]
            rsar = arr[mp:r]
            pw = arr[mp]
            num = n**mp
            if num == m:
                return mp
            if m < num:
                arr = arr[l : mp + 1]
                return root_helper(arr, l, mp)
            else:
                return root_helper(arr, mp, r)
        return root_helper(arr, 0, len(arr))


x = Root()
print(x.NthRoot(3, 27))