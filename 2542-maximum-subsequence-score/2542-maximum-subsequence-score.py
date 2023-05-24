class Solution:
    def maxScore(self, nums1, nums2, k):
        total = res = 0
        heap = []
        #default min heap
        zip_pairs = zip(nums1, nums2)#paired each ele of two list
        sorted_pairs = sorted(zip_pairs, key=lambda x: -x[1])#sorted based on nums2
        for i in sorted_pairs:
            print(i)
        for pair in sorted_pairs:#iterate to all pairs and find max
            num1, num2 = pair  
            heappush(heap, num1)
            total += num1
            if len(heap) > k: #if len > k means pop the first ele (i.e min ele)
                total -= heappop(heap)
            if len(heap) == k: #checking for max val if len==k
                res = max(res, total * num2) #total holds the sum of k nums1 ele
        
        return res