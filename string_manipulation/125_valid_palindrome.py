class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]   # only alphabet, number
        reverse_s = s[::-1]

        if reverse_s == s:
            return True
        else:
            return False
        # return reverse_s == s
