"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        import itertools
        indices  = itertools.product(range(len(s)-1),range(1,len(s)) )
        indices = [ i  for i in indices if i[0] < i[1] ]
    
        final = ""
        maxLength = 0 
        
        if(len(s)==0):
             return ""
        if(len(s)==1):
            return s
        
        
        for index in indices:
            
            if (self.checkPalindrome(s[index[0]:index[1]]) == True):
                   if(maxLength < len(s[index[0]:index[1]])):
                      final =s[index[0]:index[1]]
                      maxLength = len(final)
       
        return final
    
    #Function to check if a selected substring is a palindrome    
    def checkPalindrome(self,s):
        count = 0
        for i in range(len(s)//2):
            
            if (s[i]==s[len(s)-i-1] ):
                  count +=1 
            
        if(count == len(s)//2):
             return True
        else :
             return False
