
"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
"""


class Solution:
    def reorganizeString(self, S: str) -> str:
        import heapq
        dict= {}
        final = ""
        for i in range(len(S)):
            if S[i] not in dict:
                dict[S[i]] = 1
            else:
                dict[S[i]] +=1
    
        hip = [ [-value,key] for key,value in dict.items()]
        heapq.heapify(hip)
        while(hip):

             first = heapq.heappop(hip)
             if hip:   
               second = heapq.heappop(hip) 
             else:
                if first[0] < -1 :
                      return ""
                else:
                      final+= first[1]
                      return final
             final += first[1] + second[1]
             first[0] += 1
             second[0] += 1
             if(first[0] < 0):
               heapq.heappush(hip,[first[0],first[1]])   
             if second[0] < 0:
               heapq.heappush(hip,[second[0],second[1]]) 
        return final
            
             