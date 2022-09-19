from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            letters = sorted(s)
            hashMap[tuple(letters)].append(s)
        return hashMap.values()