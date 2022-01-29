class Solution:
    def reverse(self, x: int) -> int:
        
        limit = 2**31 # Since there is integer range : 2^31
        
        def reverse_num(n):
            reverse = 0
            n = abs(x) # converting negetive number into positive
            while n != 0:
                remainder = n % 10
                reverse = reverse * 10 + remainder
                n = int(n / 10)

            if reverse <= -limit or reverse >= limit-1:
                return 0
            
            return reverse
                
        
        if x < 0:
            return -reverse_num(x)
        else:
            return reverse_num(x)
        