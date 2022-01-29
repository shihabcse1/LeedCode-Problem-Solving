class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        str_len = len(strs)
        
        if str_len == 0:
            return ""
        elif str_len == 1:
            return strs[0]
        else:
            strs.sort() 
            first_item = strs[0]
            last_item = strs[-1]
            cnt = 0
            
            for i in range(len(first_item)):
                if strs[0][i] == strs[-1][i]:
                    cnt += 1
                else:
                    break
                    
            
            lcs = first_item[0:cnt]
                    
        return lcs