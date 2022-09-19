from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            letters = sorted(set(s))
            freq = [s.count(l) for l in letters]
            letters.extend(freq)
            hashMap[tuple(letters)].append(s)
        return hashMap.values()