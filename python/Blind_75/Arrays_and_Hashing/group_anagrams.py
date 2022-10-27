from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for letter in s:
                count[ord(letter) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()

        # Time: O(m*n)




        # attempted solution
        # anagrams = []
        # sortedStrs = []

        # for s in strs:
        #     s = sorted(s)
        #     sortedStrs.append("".join(s))

        # for i in range(len(sortedStrs)):
        #     sub = []
        #     for j in range(len(sortedStrs)):
        #         if i != j:
        #             print("i", i)
        #             print("j", j)
        #             if sortedStrs[i] == sortedStrs[j]:
        #                 sub.append(strs[j])
        #     sortedStrs.remove(sortedStrs[i])
        #     sub.append(strs[i])

        #     print(sub)