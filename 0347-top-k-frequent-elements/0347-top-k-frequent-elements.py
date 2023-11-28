from collections import Counter, defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        
        count = Counter(nums)
        for num, freq in count.items():
            if len(h) < k:
                heappush(h, (freq, num))
            elif freq > h[0][0]:
                heappop(h)
                heappush(h, (freq, num))
        return [entry[1] for entry in h[:k]]
#         bucket = [[] for _ in range(len(nums)+1)]
#         
#         for num, freq in count.items():
#             bucket[freq].append(num)
        
#         print(bucket)
#         flat_list = [item for sublist in bucket for item in sublist]
#         return flat_list[-k:]
    
        element_freq = {}  # Dict[element, freq]
        for n in nums:
            element_freq[n] = element_freq.get(n, 0) + 1

        # optimization so that bucket gets initialized with only max freq
        buckets = [[] for _ in range(max(element_freq.values()) + 1)]
        for n, freq in element_freq.items():
            buckets[freq].append(n)
        flat_list = [n for bucket in buckets for n in bucket]

        return flat_list[-k:]
        
        
        
        
        
        