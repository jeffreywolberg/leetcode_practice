class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        output = set()
        mapNums = {}
        mapTwoSum = defaultdict(list)
        for i in range(len(nums)):
            n1 = nums[i]
            mapNums[n1] = i
            for j in range(len(nums)):
                if i == j:
                    continue
                n2 = nums[j]
                mapTwoSum[n1 + n2].append([i, j])
            
        for k, all_inds_two_sum in mapTwoSum.items():
            for inds_two_sum in all_inds_two_sum:
                if -k in mapNums:
                    ind_num = mapNums[-k]
                    n1, n2, n3 = -k, nums[inds_two_sum[0]], nums[inds_two_sum[1]]
                    # print(-k, ind_num, inds_two_sum)
                    if ind_num not in inds_two_sum:
                        # print([ind_num, *inds_two_sum])
                        output.add(tuple(sorted([n1, n2, n3])))

        return output
    
    
    def threeSum(self, nums):
        dups = set()
        seen = {}
        output = set()
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                # seen[val1] = 1
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        # and seen[complement] == i:
                        output.add(tuple(sorted([val1, val2, complement])))
                    
                    seen[val2] = i
                    
        return output

    def twoSum(self, nums, i, j, target):
        hashset = {}
        output = []
        while(i < j):
            num_sum = nums[i] + nums[j]
            if num_sum == target:
                output.append([i, j])
                i += 1
                j -= 1
            elif num_sum < target:
                i += 1
            elif num_sum > target:
                j -= 1
            
        return output
            
    
    def threeSum4(self, nums):
        nums = sorted(nums)
        print(nums)
        output = set()
        for i, n in enumerate(nums):
            if n > 0:
                return output
            if i == 0 or nums[i] != nums[i-1]:
                target = -nums[i]
                print(target)
                valid_inds = self.twoSum(nums, i+1, len(nums)-1, target)
                for i_sol, j_sol in valid_inds:
                    output.add(tuple(sorted([nums[i_sol], nums[j_sol], nums[i]])))
        
        return output
                
            
        
                    
                
                    
                    
                