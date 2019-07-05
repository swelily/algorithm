def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
    for i in t:
        dic[i] = dic.get(i, 0) - 1
        if dic[i] < 0:
            return False
    return True



