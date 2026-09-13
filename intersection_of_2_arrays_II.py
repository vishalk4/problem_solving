class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        r = []
        for i in range(0,len(nums1)):
            # check if the key already exist
            if nums1[i] not in d: 
                d[nums1[i]] = 0 
            # if already exist then increase its count
            d[nums1[i]] += 1
        for i in range(0,len(nums2)):
            # now check if the elements exist in nums2 
            if nums2[i] in d and d[nums2[i]] != 0:
                # if exist append it to result list andecrement the count of the element
                r.append(nums2[i])
                d[nums2[i]]-=1
        return r

