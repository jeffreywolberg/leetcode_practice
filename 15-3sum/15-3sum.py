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
            
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        output.add(tuple(sorted([val1, val2, complement])))
                    
                    seen[val2] = i
                    
        return output
                        
                
            
        
                    
                
                    
                    
                