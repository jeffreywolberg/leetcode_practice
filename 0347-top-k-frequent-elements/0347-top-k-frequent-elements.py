from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """v3: bucket sort"""
        element_freq = {}  # Dict[element, freq]
        for n in nums:
            element_freq[n] = element_freq.get(n, 0) + 1

        buckets = [[] for _ in range(max(element_freq.values()) + 1)]
        for n, freq in element_freq.items():
            buckets[freq].append(n)
        flat_list = [n for bucket in buckets for n in bucket]

        return flat_list[-k:]
        
        
        
        
        
        