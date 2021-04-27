"""
class Solution:
    def __init__(self, w: List[int]):
        self.w__w=w
        
        l=[]
        for i,c in enumerate(w):
            for x in range(c):
                l.append(i)
        self.__l = l
        
    def pickIndex(self) -> int:
        return self.__l[random.randrange(len(self.__l))]

rather than really build a list to record  freqnency we build a accumlation list to minimize the size of the table
"""
class Solution:
    def __init__(self, w: List[int]):
    
        a=[None]*len(w)
        a[0] = w[0]
        for i in range(1,len(w)):
            a[i]=a[i-1]+w[i]
        self.__a=a
    
        
    def pickIndex(self) -> int:
        temp= random.randrange(self.__a[-1]) #a[-1]->len(a)
        for i,c in enumerate(self.__a):
            if(temp<c):
                return i