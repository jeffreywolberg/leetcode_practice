class Solution:
    def getVolume(self, iLeft, iRight, height: List[int]):
        return (iRight - iLeft) * min(height[iRight], height[iLeft])
    
    def maxArea(self, height: List[int]) -> int:
        maxVolume = -1
        iLeftBest = -1
        iRightBest = -1

        iLeft = 0
        iRight = len(height) - 1
        while iLeft < iRight:
            box_volume = self.getVolume(iLeft, iRight, height)
            if box_volume > maxVolume:
                iLeftBest = iLeft
                iRightBest = iRight
                maxVolume = box_volume
            if height[iLeft] < height[iRight]:
                iLeft += 1
            else:
                iRight -= 1
        return maxVolume
        