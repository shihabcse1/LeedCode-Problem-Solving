class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        
        if needle_len == 0:
            return 0
        else:
            return haystack.find(needle) # find fuction return -1 if that string isn't found