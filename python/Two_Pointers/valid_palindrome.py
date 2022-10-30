class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_copy = []

        for letter in s:
            num = ord(letter)
            if (num >= 97 and num <= 122) or (num >= 48 and num <= 57):
                s_copy.append(num)
            elif num >= 65 and num <= 90:
                num += 32
                s_copy.append(num)
        
        return s_copy == s_copy[::-1]