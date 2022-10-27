class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countDict[n] = 1 + countDict.get(n, 0)
        
        for n, c in countDict.items():
            frequency[c].append(n)

        res = []

        for i in range(len(frequency) - 1, 0 , -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        # Time: O(n)


Solution().topKFrequent( nums=[1,1,1,2,2,3, 200],k=2)
