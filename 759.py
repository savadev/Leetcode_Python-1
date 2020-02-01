"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
 
 
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:

schedule and schedule[i] are lists with lengths in range [1, 50].
0 <= schedule[i].start < schedule[i].end <= 10^8.
NOTE: input types have been changed on June 17, 2019. Please reset to default code definition to get new method signature.
"""



"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        input = [[element.start,element.end] for row in schedule for element in row]
        input = sorted(input, key = lambda x:x[0])
        i = 1 
        final = []
        left = input[0][0]
        right = input[0][1]
        while i < len(input):
              if input[i][0] <= right: 
                     if input[i][1] <= right :
                            i+=1
                            continue
                     else:
                          left = input[i][0]
                          right = input[i][1]
                          
              else:
                      final.append([right,input[i][0]])
                      left = input[i][0]
                      right = input[i][1]  
              i+=1
        final = [Interval(element[0],element[1]) for element in final ]
        return final