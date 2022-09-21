class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        keys = set(nums)
        longest_seq = []
        while len(keys) != 0:
            n = keys.pop()
            seq = [n]
            i = 1
            while n-i in keys:
                seq.append(n-i)
                keys.remove(n-i)
                i += 1
            i = 1
            while n+i in keys:
                seq.append(n+i)
                keys.remove(n+i)
                i += 1
                
            if len(seq) > len(longest_seq):
                longest_seq = seq
                
        return len(longest_seq)
            
            
                
            
        