class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key = lambda x : x[0])
        if len(intervals) <= 1:
            return True

        cur_end = intervals[0][1]
        for prev, end in intervals[1:]:
            if prev < cur_end:
                return False
            cur_end = end
        return True



