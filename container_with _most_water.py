class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        mw = 0 # variable to store maximum water
        while left < right: # loop until pointers meet
            width = right - left # width between the two lines
            # height is the length of shorter line
            ch = min(height[left], height[right])
            # calculate current area
            cw = width * ch
            # update maximum water if current is larger
            mw = max(mw, cw)
            # move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mw
