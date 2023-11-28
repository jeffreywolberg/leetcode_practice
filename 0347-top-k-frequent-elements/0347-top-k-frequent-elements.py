from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)
        for num, freq in count.items():
            bucket[freq].append(num)
        
        print(bucket)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[-k:]
        
        
        
        
        
        