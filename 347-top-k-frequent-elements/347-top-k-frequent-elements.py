from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMapFreq = defaultdict(list)
        hashMapLetter = defaultdict(int)
        for n in nums:
            hashMapLetter[n] += 1
            if hashMapLetter[n] > 1:
                hashMapFreq[hashMapLetter[n]-1].remove(n)
            hashMapFreq[hashMapLetter[n]].append(n)
            
        freqKeys = list(hashMapFreq.keys())
        output = []
        for key in freqKeys[::-1]:
            for n in hashMapFreq[key]:
                output.append(n)
                if len(output) == k:
                    return output

                
            
            
        