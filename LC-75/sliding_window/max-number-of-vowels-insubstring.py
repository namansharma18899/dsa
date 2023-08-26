class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = {each:0 for each in ['a','e','i','o','u']}
        max_vow = -99
        for index in range(0, len(s)):
            if index<k:
                if s[index] in vowel_count:
                    vowel_count[s[index]]+=1
                    count = 0
                    for key,v in vowel_count.items(): count+=v
                    max_vow = max(max_vow, count)
                continue
            prev_el = index - k
            if s[prev_el] in vowel_count:
                vowel_count[s[prev_el]]-=1
            if s[index] in vowel_count:
                vowel_count[s[index]]+=1
            count = 0
            for key,v in vowel_count.items(): count+=v
            max_vow = max(max_vow, count)
        return max_vow


sol = Solution()

s = "tryhard"
k = 4

print(sol.maxVowels(s, k))