from collections import Counter 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = Counter()
        for n in nums:
            hashMap[n] += 1
        
        print(hashMap)
        longest_seq = []
        while len(keys:=hashMap.keys()) != 0:
            n = hashMap.popitem()[0]
            seq = [n]
            i = 1
            while n-i in keys:
                seq.insert(0, n-i)
                hashMap.pop(n-i)
                i += 1
            i = 1
            while n+i in keys:
                seq.append(n+i)
                hashMap.pop(n+i)
                i += 1
            if len(seq) > len(longest_seq):
                longest_seq = seq
        print(longest_seq)
                
        return len(longest_seq)
            
            
                
            
        