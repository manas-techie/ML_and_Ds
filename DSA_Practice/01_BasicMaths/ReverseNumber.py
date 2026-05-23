class Solution:
    def ReverseNumber(self, num):
        rev_num = 0
        while num > 0:
            digit = num % 10
            rev_num = rev_num * 10 + digit
            num = num // 10

        return rev_num
    
solution = Solution() 
print(solution.ReverseNumber(123))