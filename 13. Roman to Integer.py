class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbols = {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        num = 0
        str_len = len(s)
        
        for i in range(str_len):
            if i > 0 and symbols[s[i]] > symbols[s[i-1]]:
                num = num + (symbols[s[i]] - 2 * symbols[s[i-1]])
            else:
                num = num + symbols[s[i]]

        return num