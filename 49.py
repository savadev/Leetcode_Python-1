"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        final = []
        for stri in strs:
            key = "".join(sorted(stri))
            
            if(dict.get(key) == None):
               dict[key] = [stri]
            else:    
               dict[key].append(stri) 
        
        for key in dict:
            print(dict[key])
            final.append(dict[key])
        return final
            
