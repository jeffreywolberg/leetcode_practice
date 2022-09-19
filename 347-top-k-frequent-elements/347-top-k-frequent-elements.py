from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        hashMapFreqLetter = defaultdict(list)
        hashMapLetterFreq = defaultdict(int)
        for n in nums:
            hashMapLetterFreq[n] += 1
            if hashMapLetterFreq[n] > 1:
                hashMapFreqLetter[hashMapLetterFreq[n]-1].remove(n)
            hashMapFreqLetter[hashMapLetterFreq[n]].append(n)
            
        freqKeys = list(hashMapFreqLetter.keys())
        output = []
        for key in freqKeys[::-1]:
            for n in hashMapFreqLetter[key]:
                output.append(n)
                if len(output) == k:
                    return output
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k: return nums
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)
        
                
            
            
        