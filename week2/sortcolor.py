class Solution:
    def sortColors(self, nums: List[int]) -> None:
        R=0
        W=0
        B=0
        for count in range(len(nums)):
            if(nums[count]==0):R+=1
            if(nums[count]==1):W+=1
            if(nums[count]==2):B+=1
        
        for i in range(R):
            nums[i]=0
        
        
        for i in range(R,R+W):
            nums[i]=1
        
        
            
        for i in range(R+W,R+W+B):
            nums[i]=2
            
    
        