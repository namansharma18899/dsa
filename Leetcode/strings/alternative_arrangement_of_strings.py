def alter(s1: str, s2: str)-> str:
    abs_len = len(s1) if len(s1)>len(s2) else len(s2)
    res = list()
    for char_len in range(abs_len):
        if char_len<len(s1):
            res.append(s1[char_len])
        if char_len<len(s2):
            res.append(s2[char_len])
    return ''.join(res)


print(alter('XY', 'ABCD'))