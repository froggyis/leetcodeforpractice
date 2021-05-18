def searchInsert(nums,left,right, target):
    if left == right: return left
    mid = (left + right)//2
    if(nums[mid]==target): return mid
    if(nums[mid]>target): return searchInsert(nums,left,mid,target)
    if(nums[mid]<target): return searchInsert(nums,mid+1,right,target)
   
    
    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        print((0+1)//2)
        return searchInsert(nums,0,len(nums),target)