class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        while left <= right:
            # partition nums1
            partition1 = (left + right) // 2
            # partition nums2
            # total elements on the left side should be half
            partition2 = (m + n + 1) // 2 - partition1
            # elements just before and after the partitions
            # use -infinity / +infinity for boundary cases
            if partition1 == 0:
                maxLeft1 = float('-inf')
            else:
                maxLeft1 = nums1[partition1 - 1]
            if partition1 == m:
                minRight1 = float('inf')
            else:
                minRight1 = nums1[partition1]
            if partition2 == 0:
                maxLeft2 = float('-inf')
            else:
                maxLeft2 = nums2[partition2 - 1]
            if partition2 == n:
                minRight2 = float('inf')
            else:
                minRight2 = nums2[partition2]
            # check whether we found the correct partition
            # everything on the left must be <= everything on the right
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # total number of elements is even
                if (m + n) % 2 == 0:
                    # median = average of the two middle values
                    return (max(maxLeft1, maxLeft2)+ min(minRight1, minRight2)) / 2
                # total number of elements is odd
                else:
                    # median is the largest value on the left
                    return max(maxLeft1, maxLeft2)
            # nums1 partition is too far to the right
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            # nums1 partition is too far to the left
            else:
                left = partition1 + 1
