class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = list(s.split())
        length = len(wordList[-1])
        print (length)
        return length
#  类里面的函数就是方法 method

objectSolution = Solution()
s = str(input ("输入一串字符串，中间以空格间隔： "))
objectSolution.lengthOfLastWord(s)




# def function():
#     strings = str(input("输入字符串，以空格分隔： "))
#     wordList = list(strings.split( ))
#     length = len(wordList[-1])
#     print (length)
# function()