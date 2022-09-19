class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
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
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L, R = [], []
        for i, n in enumerate(nums):
            if i == 0:
                L.append(1)
            else:
                L.append(nums[i-1]*L[i-1])
        
        nums_rev = nums[::-1]
        
        for i, n in enumerate(nums_rev):
            if i == 0:
                R.append(1)
            else:
                R.append(nums_rev[i-1]*R[i-1])
        
        R = R[::-1]
        output = []
        for i in range(len(nums)):
            output.append(R[i] * L[i])
            
        print(nums)
        print(L)
        print(R)
        print(output)
        return output
                
            
    
            
        