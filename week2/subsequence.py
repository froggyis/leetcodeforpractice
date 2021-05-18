class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        if(len(s)==0 ): return True
        i=0
        j=0
        
        
        for count in range (len(t)):
            if(i==len(s)): return True
            if(s[i]==t[j]):
                i=i+1
            j=j+1
            
        if(i== len(s)): return True
        return False