
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<=0): return False
        
        temp = math.log2(n)
        
        temp_int = int(temp)
        temp_float=float(temp)
        if(temp_int == temp_float ): return True
        return False