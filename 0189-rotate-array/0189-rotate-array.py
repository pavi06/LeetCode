class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        l,r=0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]  #reverse the whole array
            l,r=l+1,r-1
        
        l,r=0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]  #reverse the first half
            l,r=l+1,r-1
            
        l,r=k,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]  #reverse the second half
            l,r=l+1,r-1
            
# for one sapce this logic is used        
            
        