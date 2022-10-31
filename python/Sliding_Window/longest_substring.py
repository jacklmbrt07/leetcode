from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        pos = defaultdict(int)

        start = 0

        for end, char in enumerate(s):
            start = max(start, pos[char])
            max_len = max(max_len, end - start + 1)
            pos[char] = end + 1

        return max_len