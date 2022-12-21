class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i in nums2:
                s=nums2.index(i)
                s+=1
                while(s<len(nums2)):
                    if nums2[s]>i:
                        l.append(nums2[s])
                        break
                    s+=1
                else:
                    l.append(-1)
            else:
                l.append(-1)
        return l
                        
                
                
        