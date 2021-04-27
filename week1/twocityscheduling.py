def diff(l):
    return l[0]-l[1]

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=diff)
        print(costs)
        count=0
        countA=0
        ans=0
        
        for costA,costB in costs:
            if( count< len(costs)//2 ):
                ans+=costA
                count=count+1
                
            else:
                ans+=costB
            
        return ans
        
        
