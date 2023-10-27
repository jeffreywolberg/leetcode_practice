class Solution:

    def is_overlapping(self, ns, ne, os, oe):
        if ne < os:
            return False
        elif ns > oe:
            return False
        return True
    

                


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0: 
            return [newInterval]
        
        ns, ne = newInterval
        
        out = []
        for i in range(len(intervals)):
            ns, ne = newInterval
            cur_s, cur_e = intervals[i]
            if cur_s > ne:
                return out + [newInterval] + intervals[i:]
            elif ns > cur_e:
                out.append(intervals[i])
            else:
                newInterval = [min(ns, cur_s), max(ne, cur_e)]
        
        return out + [newInterval]
            
            

        

                

        
        return intervals


        
            
            
        
        