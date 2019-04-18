class Solution:
    
    def __init__(self):
         self.teleDict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
         self.combinationList = []
        
    def createCombos(self,com,digits):
        if len(digits) == 0:
            self.combinationList.append(com) 
        else:
            for c in self.teleDict[digits[0]]:
                self.createCombos(com + c, digits[1:])
            
    def letterCombinations(self, digits):
            if digits:
                self.createCombos('',digits)
            return self.combinationList
