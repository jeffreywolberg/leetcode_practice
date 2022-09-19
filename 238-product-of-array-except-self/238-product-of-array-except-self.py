class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_prod = 1
        has_zero = False
        for n in nums:
            # first time seeing a zero
            if n == 0 and not has_zero:
                has_zero = True
                continue
            total_prod *= n
        
        for i, n in enumerate(nums):
            if nums[i] == 0:
                output.append(total_prod)
            elif has_zero:
                output.append(0)
            else:
                output.append(int(total_prod * (nums[i]**(-1))))
        
        return output
            
        