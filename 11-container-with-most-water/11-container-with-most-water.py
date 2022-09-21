def area(height, i, j):
    return (j-i) * min(height[i], height[j])

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        
        max_area = 0
        
        while(i < j):          
            containerArea = area(height, i, j)
            if containerArea > max_area:
                max_area = containerArea
                
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        
        return max_area
        