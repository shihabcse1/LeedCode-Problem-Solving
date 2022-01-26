class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_num = 0
        n = x
        if x < 0:
            return False
        else:
            while n != 0:
                remainder = n % 10
                reverse_num = reverse_num * 10 + remainder
                n = int(n / 10)
            
            if reverse_num == x:
                return True
            else:
                return False