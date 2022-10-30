class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        # s_arr = list(s)
        # t_arr = list(t)

        # s_arr.sort()
        # t_arr.sort()

        # if s_arr == t_arr:
        #     return True
        # return False

        # Time: O(n log n)
        # Space: O(1)

        # Solution 2

        # if len(s) != len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = countS.get(s[i], 0) + 1
        #     countT[t[i]] = countT.get(t[i], 0) + 1

        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False

        # return True

        # Solution 3

        # return Counter(s) == Counter(t)

        # Solution 4

        return sorted(s) == sorted(t)

        # Time: O(n log n)
        # Space: O(1)