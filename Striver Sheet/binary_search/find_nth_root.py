def NthRoot(n: int, m: int):
    powers = [ind for ind in range(100)]

    def root_helper():
        mp = l + (r - l)/2
        if len(powers)<=2:
        lsar  = powers[l:mp+1]
        rsar =  powers[mp:r+1]
        pw = powers[mp]
        num = n**mp
        if num == m:
            return mp 
        if m< num:
            powers  = powers[l: mp+1]
            return root_helper(l, mp) 
        else:
            return root_helper(mp, r)